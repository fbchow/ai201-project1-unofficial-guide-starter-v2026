"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def _recursive_split(text: str, chunk_size: int, separators: list[str]) -> list[str]:
    """
    Split `text` on the first separator that appears in it, then recurse on
    any piece that's still too big, moving down the separator list.

    Separators are tried in order (paragraph breaks, then line breaks, then
    words). If none of them appear, or we run out of separators, fall back to
    a hard character-level cut — the same thing `fallback_split` does.
    """
    if len(text) <= chunk_size:
        return [text] if text else []

    if not separators:
        return [
            text[start : start + chunk_size]
            for start in range(0, len(text), chunk_size)
        ]

    separator, rest = separators[0], separators[1:]
    if separator not in text:
        return _recursive_split(text, chunk_size, rest)

    pieces: list[str] = []
    for part in text.split(separator):
        if not part.strip():
            continue
        if len(part) <= chunk_size:
            pieces.append(part)
        else:
            pieces.extend(_recursive_split(part, chunk_size, rest))
    return pieces


def _merge_pieces(pieces: list[str], chunk_size: int, overlap: int) -> list[str]:
    """
    Greedily glue small pieces back together (paragraph by paragraph) up to
    `chunk_size`, so a chunk isn't just one short paragraph. Each new chunk
    is seeded with the tail of the previous one so neighbouring chunks share
    `overlap` characters of context.
    """
    chunks: list[str] = []
    current = ""
    for piece in pieces:
        candidate = f"{current}\n\n{piece}" if current else piece
        if len(candidate) <= chunk_size:
            current = candidate
            continue

        if current:
            chunks.append(current)
            tail = current[-overlap:] if overlap else ""
            current = f"{tail}\n\n{piece}" if tail else piece
        else:
            current = piece

    if current:
        chunks.append(current)

    return chunks


def split_documents(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    Split documents into chunks using a simple recursive character splitter.

    Line breaks ("\\n") are the primary split point. Any line still longer
    than `chunk_size` is recursively re-split on spaces, falling back to a
    hard character cut only as a last resort. Small pieces are then merged
    back together up to `chunk_size`, so a short line isn't stranded as its
    own tiny chunk, and neighbouring chunks share `overlap` characters of
    context.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        pieces = _recursive_split(doc.text, chunk_size, ["\n", " "])
        for index, text in enumerate(_merge_pieces(pieces, chunk_size, overlap)):
            text = text.strip()
            if text:
                chunks.append(
                    Chunk(
                        text=text,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::split_documents",
                    )
                )

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
