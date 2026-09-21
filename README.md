# The Unofficial Guide
## Campus Life
<!-- Replace this line with your name and which corpus you picked. -->

---

# Unit 1

## What This Does
This system answers questions about university campus life from a collection of short 88 documents. The documents are parsed into chunks by new line, and these units of information are sourced to answer user questions. Campus life topics, include transportation, housing, courses, library. If the sytem does not know the answer to a question, it will say so rather than make up an answer.  

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** 320
**Overlap:** 0

Since the average character length of each document was 317 characters, I picked 320 characters as a chunk size. If that's the average for each document then in general, each paragraph will have less than 320 characters per new line or paragraph.

Both the questions and answers I propose straight-forward and short. They can be deduced from each new line of info in a document. Since I don't expect the information to come from multiple lines and multiple paragraphs, I tried recursive character text splitting on the new line "\n" character. This eliminates the need for overlap because a new line is such a clear delimiter you don't need extra overlap padding characters as back-up in case your chunks overlap in an awkward way.  

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->


```
                    
129 chunks total. Showing 5, spread across the corpus.

Paste these into your README under Sample Chunks. The rubric asks
for the source file and the function that produced them — both are
printed for you below.

======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

======================================================================
Chunk 2  |  source: course_cs_210_exams.txt#0  |  produced by: chunker.py::split_documents
======================================================================
CS 210 Data Structures — assessment

Two midterms and a final, all drawn from lecture material rather than the textbook. Midterms are curved, the final is not.

Do the labs even though they're only 10% — the exams reuse the lab problems.

======================================================================
Chunk 3  |  source: course_phys_130_workload.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Workload for PHYS 130 Mechanics

People keep asking so: 7 hours a week, plus 3 on lab weeks. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

======================================================================
Chunk 4  |  source: dining_the_ridgeway_cafe.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Hours are 7:00am to 4:00pm weekdays only. Costs declining balance only, no meal swipes.

======================================================================
Chunk 5  |  source: housing_morrow_house.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Morrow House — what it's actually like

Just finished a year in this building. Built 1954, partially renovated 2008. Rooms are singles and doubles, hall bathrooms.

The good: cheapest housing tier by about $900 a year, and the singles are real singles.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"How often does the bus shuttle run on Saturday?"

**Answer:**

```
python app.py ask "How often does the bus shuttle run on Saturday?" --show-prompt

(best distance 0.301, cutoff 0.6)
======================================================================
System instruction sent with the prompt
======================================================================
You answer questions using only the documents provided to you.

Rules:
- Use only the information in the documents below. Do not use anything you know from elsewhere.
- If the documents don't cover the question, say you don't have enough information. Do not guess.
- Name the document your answer came from, using the filename given in each excerpt.
- Be brief. Two or three sentences is usually enough.

======================================================================
The assembled prompt, exactly as sent
======================================================================
Documents:

[from transit_shuttle.txt]
The campus shuttle

Runs a loop every 20 minutes from 7am to 11pm on weekdays and every 40 minutes on weekends. The published timetable is optimistic by about five minutes in the morning and accurate the rest of the day.

[from winter_gear.txt]
The paths get cleared by 7am on weekdays and considerably later on weekends.

[from dining_kestrel_commons.txt]
Hours are 7:00am to 9:00pm weekdays, 9:00am to 8:00pm weekends. Costs one meal swipe, or $12.50 cash.

---

Question: How often does the bus shuttle run on Saturday?

Answer using only the documents above, and name the file you used.
======================================================================

Based on the campus shuttle document, the shuttle runs every 40 minutes on weekends (transit_shuttle.txt).

Sources retrieved: dining_kestrel_commons.txt, transit_shuttle.txt, winter_gear.txt
```

**My relevance cutoff:** 0.55
It looks like a clear boundary around 0.5 is forming for the in corpus document questions. And the obviously random questions out of context are above 0.8. I picked 0.55 in case to stay clear of rounding error in from the highest distance of 0.498 might have as it is rounded to 0.5 or trailing digits.  

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| What time is the library open until during the term? | ✅ |0.409  |
| How often does the bus shuttle run on Saturdays? | ✅|0.498  |
| How much cloud storage do students get on student accounts? | ✅ |0.292  |
| When do library and dining jobs get posted? | ✅ |0.409  |
| When is the best time to do laundry in Alridge Hall? | ✅ |0.416|
| What is the capital of Mongolia?| ❌ | 0.825
| How do I change the oil in a diesel engine?| ❌ | 0.934
| Who won the 1994 World Cup? | ❌ | 0.874 |
| What is the recommended dosage of ibuprofen for a headache?| ❌ | 0.824
| How do I write a for loop in Rust? | ❌ | 0.891



## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** 
I asked Claude to write the recursive character split function. I learned about this chunking strategy from [this Youtube video](https://www.youtube.com/watch?v=8OJC21T2SL4&t=964s) and [this dev.to blog post](https://dev.to/eteimz/understanding-langchains-recursivecharactertextsplitter-2846). Most examples online, like [this denser.ai blog post](https://denser.ai/blog/rag-chunking-strategies/), use the `RecursiveCharacterTextSplitter()` function from the LangChain library, but I did not want to import an external library. I asked Claude to implement a simple recursive character split function that splits chunks by new lines because that's how my answers will look like.  


**2.**
I asked Claude to clarify how the recursive character splitting logic works: "In the simplest terms, explain how recurisve character splitting works as an algorithm. how does the chunk size and overlap size get factored in?"

The response:
```
Recursive character splitting works like this, in plain terms:

Try to cut the text at a "nice" boundary. It has a priority list of separators — usually paragraph breaks (\n\n) first, then line breaks (\n), then spaces ( ), then finally just individual characters as a last resort.
Split on the first separator that appears, breaking the text into a list of pieces (e.g., paragraphs).
Check each piece against chunk_size. If a piece is small enough, keep it as-is. If a piece is still too big, recurse: try splitting that piece using the next separator down the list (e.g., paragraph → lines → spaces → characters).
This repeats until every piece fits under chunk_size.
Where chunk_size comes in: it's the ceiling — the algorithm keeps re-splitting on smaller and smaller boundaries only until each piece is ≤ chunk_size. It's the trigger for "is this piece done, or does it need to be cut further?"

Where overlap comes in: it's not part of the splitting step at all — it's applied afterward, during merging. Once you have small pieces, you glue them back together up to chunk_size to avoid tiny stray chunks. When starting a new chunk, you seed it with the last overlap characters of the previous chunk, so consecutive chunks share some context instead of cutting off mid-thought at the boundary.

In this codebase, that's exactly what _recursive_split (splitting) and _merge_pieces (merging + overlap) do, called from split_documents.
```



<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
