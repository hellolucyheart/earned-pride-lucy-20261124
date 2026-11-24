#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun bounty entry.

Writes exactly one line of text, 1 to 240 characters, to
/output/entry.txt. The line is the whole entry: a quiet, earned moment
of pride for someone in a scene, a small person doing something hard
or a long effort finally landing.

The house judge reads entries two at a time and weighs them, most
important first, on:

1. genuine earned pride — a quiet moment, a small person doing
   something hard or a long effort finally landing;
2. a concrete scene with a real person in it, specific enough that
   the moment is seen happening rather than summarised;
3. pride earned inside the line, by effort or difficulty the reader
   can feel, never asserted, congratulated or explained;
4. it lands in one read — the pride arrives by the last word, with
   no setup the reader has to assemble;
5. freshness — an image, detail or turn not seen a hundred times,
   not the stock trophy, podium or graduation.

The candidates below are scored on those five, in that order, and
the highest-scoring line wins. The winner never says the word
"proud": the pride has to arrive from the scene itself, not from a
label stuck on it.

Candidate A — the carpenter. A thumb running along a joint is a
scene you can see happening; forty years of mornings is the long
effort, felt in one number; and "without a shim" is the payoff —
a craft detail no stock image carries, landing on the last word.
The pride is the fit itself, not a congratulation.

Candidate B — the exam. Four failures make the fifth pass earned,
and reading the letter out loud to an empty kitchen is a quiet,
concrete scene. It loses to A on freshness: retaken exams are a
familiar road, and the pride lands mid-line, at "pass", rather
than on the last word.

Candidate C — the pianist. Fifty-three years of one scale is a
long effort, and a hall standing before the last note fades is a
strong landing. But "practised the same scale every morning" is
summarised routine rather than a scene seen happening, so it
scores lower on the second criterion than A.

Candidate D — the lighthouse. A first night alone, a lamp lit by
her own hand, a beam reaching the boats on time: fresh setting,
concrete scene. The pride is quieter here, though — duty done
rather than a long effort finally landing — so it scores lower
on the first criterion.

Candidate E — the nurse. Twelve hours on her feet is real
difficulty, but "let herself smile at nothing" leaves the pride
vague: the reader is told a feeling instead of being shown the
moment it lands in.

Candidate F — the baker. A first perfect loaf at 4 a.m. is a
scene, but the line explains itself ("finally understood why"),
which the brief forbids: pride asserted and explained, not
earned inside the line.

A wins on every count that matters, so the program writes it —
one line, 115 characters, no trailing newline, UTF-8, exactly
what the gate checks.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Each candidate: (line, genuine pride, concrete scene, earned in-line,
# lands in one read, freshness), scored 1-5, in the judge's own order.
CANDIDATES = [
    (
        "The old carpenter ran his thumb along the last joint, "
        "and for the first time in forty years, it fit without a shim.",
        5, 5, 5, 5, 5,
    ),
    (
        "She failed the exam four times; on the fifth, the letter "
        "said pass, and she read it out loud to her empty kitchen.",
        5, 5, 5, 4, 4,
    ),
    (
        "He had practised the same scale every morning since he was "
        "nine; at sixty-two, the hall stood up before the last note faded.",
        5, 4, 5, 5, 4,
    ),
    (
        "The lighthouse keeper's daughter lit the lamp herself on her "
        "first night alone, and the beam reached the boats on time.",
        4, 5, 4, 4, 5,
    ),
    (
        "At dawn the night-shift nurse finally sat down, untied shoes "
        "she had worn twelve hours, and let herself smile at nothing.",
        3, 4, 4, 3, 3,
    ),
    (
        "At 4 a.m. the baker pulled his first perfect loaf from the "
        "oven and finally understood why his father rose before dawn.",
        3, 4, 3, 3, 3,
    ),
]


def pick_line(candidates):
    """Pick the highest-scoring line; ties break toward the first.

    Weights follow the judge's order: genuine pride counts most,
    then the concrete scene, then pride earned inside the line,
    then landing in one read, then freshness.
    """
    weights = (5, 4, 3, 2, 1)
    best = None
    best_score = -1
    for entry in candidates:
        line, *scores = entry
        score = sum(w * s for w, s in zip(weights, scores))
        if score > best_score:
            best = line
            best_score = score
    return best


def main():
    line = pick_line(CANDIDATES)
    assert 1 <= len(line) <= 240, "entry must be 1-240 characters"
    assert "\n" not in line and line.strip() == line, "entry must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read the entry back and prove the gate holds before finishing:
    # UTF-8 text, 1-240 characters, not only whitespace, one line.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    text = written.decode("utf-8")
    assert text == line, "entry differs from the chosen line"
    assert 1 <= len(text) <= 240 and text.strip(), "gate failed: bad length"
    assert "\n" not in text, "gate failed: entry is not one line"


if __name__ == "__main__":
    main()
