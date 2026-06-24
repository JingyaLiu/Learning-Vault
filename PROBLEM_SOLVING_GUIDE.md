# Problem Solving Guide

> You understand the algorithm. You freeze when you see a new problem.
> This guide is the bridge between those two states.

The core issue is not intelligence — it's **not having a repeatable process**. Experts don't think faster; they follow a practiced routine. This guide gives you that routine.

---

## The 5-Step Process

Use this every single time, on every problem. Do not skip steps.

```
Step 1 → UNDERSTAND   (what is the problem actually asking?)
Step 2 → RECOGNIZE    (what pattern does this look like?)
Step 3 → PLAN         (how do I apply the pattern?)
Step 4 → CODE         (write clean, simple code)
Step 5 → VERIFY       (trace through, check edge cases)
```

---

### Step 1: UNDERSTAND — Read for the constraints, not just the story

Most people read the problem once and jump to coding. That's the mistake.

**Do this instead:**
1. Read the problem once to get the gist.
2. Read it again and extract:
   - **Input type** — array? string? linked list? number?
   - **Output type** — index? boolean? new array? count?
   - **Key constraint** — sorted? distinct? positive integers? at most k?
   - **What "optimal" means** — longest? smallest? all occurrences? first occurrence?
3. Restate the problem in your own words out loud (or in a comment).

**Red flag:** If you can't restate the problem in one sentence, you don't understand it yet.

**Example (LC 3 — Longest Substring Without Repeating Characters):**
- Input: a string
- Output: a single integer (length)
- Constraint: characters must be unique in the window
- Goal: maximize the length
- → *"Find the longest stretch of consecutive characters where none repeat."*

---

### Step 2: RECOGNIZE — Map the problem to a pattern

Look for signals in the problem description. Use the **Pattern Recognition Cheat Sheet** below.

**The key question to ask yourself:**
> "What structure does the answer have? A contiguous subarray? A pair? A path?"

Then:
> "What property does the answer need? A sum limit? No duplicates? A target value?"

Once you have those two answers, the pattern usually becomes obvious.

**If you're stuck:**
- Go through each pattern in the cheat sheet below and ask "could this possibly fit?"
- Start with the simplest pattern (brute force), then ask "what's wasteful here and how can I avoid it?"

---

### Step 3: PLAN — Write the algorithm in plain English first

**Do NOT open a code editor yet.** Write pseudocode in comments.

A plan should answer:
- What data structure do I maintain? (a window? a hash map? two pointers?)
- What do I do when I move right? (expand the window? add to a count?)
- What triggers moving left? (window invalid? found a match?)
- What do I return? (max so far? a list of positions?)

**Concrete planning template:**
```
# Data: ___________
# Loop: for right in range(len(s)):
#   - When expanding right: ___________
#   - When shrinking (condition: ___________): ___________
#   - Update answer: ___________
# Return: ___________
```

**If you can't fill in the template, go back to Step 2.**

---

### Step 4: CODE — Translate your plan line by line

Rules:
- Name variables clearly: `left`, `right`, `freq`, `max_len` — not `i`, `j`, `x`.
- Write the loop structure first (the skeleton), then fill in the body.
- If you're unsure about a detail, write a `# TODO: figure out shrink condition` comment and keep moving.

**Common trap:** Getting stuck on a detail and abandoning the whole approach. Don't. Keep the momentum; fix details after the skeleton is working.

---

### Step 5: VERIFY — Trace through manually

Pick a small example (2–5 elements) and trace your code by hand, line by line.

Check these edge cases for every problem:
- **Empty input** — empty string, empty array, n=0
- **Single element** — does your loop body even run?
- **All same elements** — e.g. `[1,1,1,1]` or `"aaaa"`
- **Answer at start/end** — don't assume the answer is in the middle

---

## Pattern Recognition Cheat Sheet

When you see these signals → try this pattern.

### Two Pointers
| Signal | Example |
|---|---|
| Array is **sorted** | "Find a pair that sums to target" |
| Looking for a **pair** or **triplet** in a sorted list | 3Sum, Two Sum II |
| Comparing characters from **both ends** | Valid Palindrome |
| Maximizing/minimizing a value between two positions | Container With Most Water |

**Mental model:** Two pointers closing in (or both moving forward) to avoid checking every combination.

---

### Sliding Window
| Signal | Example |
|---|---|
| **Substring** or **subarray** (contiguous segment) | "Find longest substring where..." |
| **"Longest"** or **"shortest"** with a constraint | "Longest without repeating chars" |
| **"At most k"** or **"at least k"** of something | "At most 2 distinct characters" |
| Fixed-size window mentioned | "Subarray of size k", "anagram of p" |

**Mental model:** A window that slides forward, expanding right and shrinking left, so you never re-examine elements unnecessarily.

**Fixed vs Dynamic:**
- Window size is given → Fixed window
- Window size depends on validity → Dynamic window

---

### Hash Map / Hash Set
| Signal | Example |
|---|---|
| **"Two elements that..."** (sum, product, difference) | Two Sum — look up complement |
| **Frequency counting** | Valid Anagram, Group Anagrams |
| **"Has it appeared before?"** | Contains Duplicate |
| Need O(1) lookup of previously seen values | Any "find pair" problem |

**Mental model:** Trade space for time. Store what you've seen so you can answer "have I seen X?" in O(1).

---

### Binary Search
| Signal | Example |
|---|---|
| Sorted array, looking for **target position** | Search in Rotated Array |
| Problem says **O(log n)** or "efficient" on sorted data | Find First/Last Position |
| **"Minimize the maximum"** or **"maximize the minimum"** | Koko Eating Bananas |
| Answer is in a **monotonic range** and you can check feasibility | Search on answer space |

**Mental model:** If you can cut the search space in half at each step, use binary search.

---

### Fast/Slow Pointers (Floyd's)
| Signal | Example |
|---|---|
| **Linked list** problem | Almost always worth considering |
| **Cycle detection** | Linked List Cycle |
| **Middle of linked list** | Middle of the Linked List |
| Finding **nth from end** | Remove Nth Node From End |

**Mental model:** Fast moves 2 steps, slow moves 1. They meet at the cycle (or fast reaches end = no cycle).

---

### Linked List Techniques
| Signal | Example |
|---|---|
| Reversing | Reverse Linked List |
| Merging two lists | Merge Two Sorted Lists |
| Modification without extra space | Use a **dummy node** at the head |
| Deletion of a node | Need pointer to the *previous* node |

**Mental model:** Always draw the pointers on paper. Pointer bugs are invisible in your head.

---

## The Brute Force Trick

If you're completely stuck after Step 2, do this:

1. **Write the brute force.** Nested loops, O(n²) or worse — doesn't matter.
2. **Ask:** *"What am I recomputing on every iteration?"*
3. **That recomputation** is exactly what the efficient data structure or technique eliminates.

**Example:**
- Brute force for "Longest Substring Without Repeating" → for every starting position, scan right until you find a repeat. O(n²).
- What's recomputed? — Every time we move left by 1, we re-scan the whole inner range.
- What eliminates it? — A hash map that tells us *instantly* where the last duplicate was. → O(n).

---

## If You're Stuck During Coding

Go through this checklist in order:

1. **Did I re-read the problem?** (Your mental model might be wrong.)
2. **Can I do brute force first?** (Get something working, then optimize.)
3. **What pattern does this look like?** (Two pointers? Window? Hash map?)
4. **Can I trace a small example by hand?** (e.g., 3-element array, 4-char string)
5. **What's the state I need to maintain?** (Frequency map? A sum? A max?)
6. **When does my loop state become invalid?** (This defines the shrink condition.)

If you're still stuck after all 6: take a breath, write what you *do* know as comments, and fill in what you can. Partial solutions in interviews show process.

---

## Common Mental Blocks

**"I don't know which pattern to use."**
→ That's normal. Go through the cheat sheet above systematically, one pattern at a time, and ask "could this fit?" for each one.

**"I understand the pattern but I can't figure out how to start the code."**
→ Fill in the plan template in Step 3. Code only after you can fill in every blank.

**"I got the general idea but the details trip me up (off-by-ones, when to update, etc.)."**
→ Trace through a tiny example (3–5 elements) before you code. Verify your update logic step by step.

**"I froze in the middle of coding."**
→ Write what you know as comments. Something like `# if char already in window, move left`. Then translate comment → code. Comments are checkpoints that stop the freezing.

**"My solution passes some tests but fails edge cases."**
→ You skipped Step 5. Always check: empty input, single element, all-same, answer at boundaries.

---

## Quick Reference Card

```
SORTED ARRAY + PAIR/TRIPLET      → Two Pointers (inward)
BOTH ENDS / PALINDROME           → Two Pointers (inward)
SUBARRAY/SUBSTRING + LONGEST     → Sliding Window (dynamic)
SUBARRAY/SUBSTRING + SIZE K      → Sliding Window (fixed)
"COMPLEMENT" / "SEEN BEFORE"     → Hash Map
FREQUENCY COUNT                  → Hash Map / Counter
SORTED + FIND POSITION           → Binary Search
"O(log n)" REQUIRED              → Binary Search
LINKED LIST + CYCLE              → Fast/Slow Pointers
LINKED LIST + MIDDLE             → Fast/Slow Pointers
LINKED LIST + MODIFICATION       → Dummy Node + Pointer Manipulation
```
