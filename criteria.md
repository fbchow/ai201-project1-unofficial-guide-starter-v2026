# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
Most of the questions are easy and fairly straight-forward. It's clear whether a numeric response is right or wrong. There's no debating time and cost quantities in the question answers. Although one of them could be considered an subjective opinion on "the best" time do laundry, so it's permissable if only one is incorrect.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**  
<!-- Why all five and not four? What about your setup makes that achievable —
     or what would have to go wrong for it not to be? -->
The corpus documents are short with straight-forward titles that describe the content. If the source fails to be named, then this signals to us that the document title is not being parced correctly. This means the system foundation is broken and needs to be looked at.  

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->

Since the corpus revolves around campus life, I think that there is always a small possibility that out-of-corpus questions could seem similar to campus life topic. For example: campus life covers food and athletics, which could potentially seem similar to sports off campus, like the World Cup. But overall, I don't want the system to make-up answer and be forthcoming enough to say "I don't know."

---

## 4. Chunks are short and less than 600 characters.  
No chunk is over 600 characters. 


<!-- YOU WRITE THIS ONE.

     How would you know if your chunks were the right size? Name something
     countable or observable.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." -->



**Why this target:**
The answers are straight-forward with a lot of heavy lifting from the corpus document title. Students value conciseness and directness in the answers. Long-winded chunks with many characters would be a negative sign that the corpus documents are not being parsed correctly.  


---

## 5. Answers do not contain profanity.  

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. -->
5 out of 5 answers to do not contain profanity or curse words that would be deemed inappropriate for a school.  


**Why this target:**
It's not acceptable to have NSFW (Not Safe for Work) language in an university campus. Inappropriate tone and word choice of the response should not tarnish the reputation of the school.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
