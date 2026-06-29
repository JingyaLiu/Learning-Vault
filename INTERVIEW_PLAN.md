# Coding Interview Plan

> **Your pace:** 2 problems/day · **Your style:** all patterns first (breadth), then circle back for more (depth).  
> **Start here:** [PROBLEM_SOLVING_GUIDE.md](PROBLEM_SOLVING_GUIDE.md) → [Pass 1 — where you are](#pass-1--all-patterns-2-problems-each).

**Last updated:** June 23, 2026  
**Current:** Pass 1 · **Day 1 complete (today)** → Day 2 tomorrow  
**Pace:** 2 problems/day · breadth first, then circle back  
**Legend:** ⭐ = FAANG frequent · ⭐⭐ = must know

---

## How This Plan Works

### Two passes, then polish

```
Pass 1 (breadth)   →  every pattern, 2 example problems     ~19 days
Pass 2 (depth)     →  every pattern, 2 more problems        ~19 days
Pass 3 (polish)    →  weak spots, ⭐⭐ cold re-solves, mocks  ~2–3 weeks
```

**Why breadth first:** you build a mental map of *all* patterns before drilling deep. When you see a new problem, you know which toolbox to open.

**Your pace:** 2 problems/day ≈ **45–60 min** total. Read notes only on **Day 1 of each pattern** (first problem's morning).

---

## Daily Routine (2 problems)

| Step | Time | What |
|---|---|---|
| 1 | 5 min | New pattern? Read `notes.md`. Same pattern? Jump to problem 1. |
| 2 | 25 min | **Problem 1** — plan in comments → code → verify |
| 3 | 25 min | **Problem 2** — same process |
| 4 | 5 min | One-line journal entry per problem |

Use [PROBLEM_SOLVING_GUIDE.md](PROBLEM_SOLVING_GUIDE.md): UNDERSTAND → RECOGNIZE → PLAN → CODE → VERIFY.

**Tired day:** 1 problem only, or re-solve yesterday's easier one from memory.

---

## Pass 1 — All Patterns (2 problems each)

~**19 study days** at 2 problems/day. One day per pattern.

Check off each day when both problems are done.

### Day 1 — Binary Search (today · Jun 23, 2026) ✓
**Read:** [binary-search/notes.md](binary-search/notes.md)

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [x] | Binary Search | [704](https://leetcode.com/problems/binary-search/) | ⭐⭐ | [01_binary_search.py](binary-search/problems/01_binary_search.py) |
| [x] | Find First and Last Position | [34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | ⭐⭐ | [02_search_first_last.py](binary-search/problems/02_search_first_last.py) |

*Pass 2 extras for this pattern: Search Insert ([LC 35](https://leetcode.com/problems/search-insert-position/)), Rotated Array ([LC 33](https://leetcode.com/problems/search-in-rotated-sorted-array/)), Min in Rotated ([LC 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/))*

---

### Day 2 — Hash Maps
**Read:** [hash-maps/notes.md](hash-maps/notes.md)

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Two Sum | [1](https://leetcode.com/problems/two-sum/) | ⭐⭐ | [01_two_sum.py](hash-maps/problems/01_two_sum.py) |
| [ ] | Valid Anagram | [242](https://leetcode.com/problems/valid-anagram/) | ⭐ | — |

---

### Day 3 — Two Pointers
**Read:** [two-pointer/notes.md](two-pointer/notes.md)

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Valid Palindrome | [125](https://leetcode.com/problems/valid-palindrome/) | ⭐ | [03_valid_palindrome.py](two-pointer/problems/03_valid_palindrome.py) |
| [ ] | Two Sum II | [167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | ⭐ | [01_pair_sum_sorted.py](two-pointer/problems/01_pair_sum_sorted.py) |

---

### Day 4 — Sliding Window
**Read:** [sliding-windows/notes.md](sliding-windows/notes.md)

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Longest Substring Without Repeating | [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | ⭐⭐ | [longest_substring_unique_3.py](sliding-windows/problems/longest_substring_unique_3.py) |
| [ ] | Find All Anagrams in a String | [438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | ⭐ | [find_anagrams_in_string_438.py](sliding-windows/problems/find_anagrams_in_string_438.py) |

---

### Day 5 — Linked Lists
**Read:** [linked-list/notes.md](linked-list/notes.md)

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Reverse Linked List | [206](https://leetcode.com/problems/reverse-linked-list/) | ⭐⭐ | — |
| [ ] | Linked List Cycle | [141](https://leetcode.com/problems/linked-list-cycle/) | ⭐⭐ | — |

---

### Day 6 — Fast & Slow Pointers
**Read:** [fast-slow-pointer/notes.md](fast-slow-pointer/notes.md)

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Middle of the Linked List | [876](https://leetcode.com/problems/middle-of-the-linked-list/) | ⭐ | — |
| [ ] | Happy Number | [202](https://leetcode.com/problems/happy-number/) | ⭐ | — |

---

### Day 7 — Stacks

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Valid Parentheses | [20](https://leetcode.com/problems/valid-parentheses/) | ⭐⭐ | — |
| [ ] | Daily Temperatures | [739](https://leetcode.com/problems/daily-temperatures/) | ⭐⭐ | — |

---

### Day 8 — Prefix Sums

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Range Sum Query Immutable | [303](https://leetcode.com/problems/range-sum-query-immutable/) | ⭐ | — |
| [ ] | Subarray Sum Equals K | [560](https://leetcode.com/problems/subarray-sum-equals-k/) | ⭐⭐ | — |

---

### Day 9 — Intervals

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Merge Intervals | [56](https://leetcode.com/problems/merge-intervals/) | ⭐⭐ | — |
| [ ] | Meeting Rooms II | [253](https://leetcode.com/problems/meeting-rooms-ii/) | ⭐⭐ | — |

---

### Day 10 — Trees

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Maximum Depth of Binary Tree | [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | ⭐⭐ | — |
| [ ] | Binary Tree Level Order Traversal | [102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | ⭐⭐ | — |

---

### Day 11 — Trees (search & validation)

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Validate Binary Search Tree | [98](https://leetcode.com/problems/validate-binary-search-tree/) | ⭐⭐ | — |
| [ ] | Lowest Common Ancestor | [236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | ⭐⭐ | — |

---

### Day 12 — Tries

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Implement Trie | [208](https://leetcode.com/problems/implement-trie-prefix-tree/) | ⭐ | — |
| [ ] | Design Add and Search Words | [211](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | ⭐ | — |

---

### Day 13 — Graphs

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Number of Islands | [200](https://leetcode.com/problems/number-of-islands/) | ⭐⭐ | — |
| [ ] | Course Schedule | [207](https://leetcode.com/problems/course-schedule/) | ⭐⭐ | — |

---

### Day 14 — Heaps

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Kth Largest Element in an Array | [215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | ⭐⭐ | — |
| [ ] | Top K Frequent Elements | [347](https://leetcode.com/problems/top-k-frequent-elements/) | ⭐⭐ | — |

---

### Day 15 — Greedy

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Best Time to Buy and Sell Stock | [121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | ⭐⭐ | — |
| [ ] | Jump Game | [55](https://leetcode.com/problems/jump-game/) | ⭐ | — |

---

### Day 16 — Backtracking

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Subsets | [78](https://leetcode.com/problems/subsets/) | ⭐⭐ | — |
| [ ] | Combination Sum | [39](https://leetcode.com/problems/combination-sum/) | ⭐⭐ | — |

---

### Day 17 — Dynamic Programming

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Climbing Stairs | [70](https://leetcode.com/problems/climbing-stairs/) | ⭐⭐ | — |
| [ ] | Coin Change | [322](https://leetcode.com/problems/coin-change/) | ⭐⭐ | — |

---

### Day 18 — Sort & Search

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Sort Colors | [75](https://leetcode.com/problems/sort-colors/) | ⭐ | — |
| [ ] | Search in Rotated Sorted Array | [33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | ⭐⭐ | — |

---

### Day 19 — Bit Manipulation & Math

| Done | Problem | LC | FAANG | Vault |
|---|---|---|---|---|
| [ ] | Single Number | [136](https://leetcode.com/problems/single-number/) | ⭐ | — |
| [ ] | Rotate Image | [48](https://leetcode.com/problems/rotate-image/) | ⭐ | — |

---

### Pass 1 rest day (Day 20)

- [ ] Skim [PROBLEM_SOLVING_GUIDE.md](PROBLEM_SOLVING_GUIDE.md) cheat sheet end-to-end
- [ ] List your 3 weakest patterns
- [ ] Optional: re-solve Two Sum + Longest Substring from memory

**Pass 1 exit criteria:**
- [ ] Touched all 19 pattern areas
- [ ] ~38 problems attempted
- [ ] Can name which pattern fits each Pass 1 problem

---

## Pass 2 — Circle Back (2 more per pattern)

Same order as Pass 1. **Do not read notes again** unless stuck — jump straight into problems.

| Day | Pattern | Problem A | Problem B |
|---|---|---|---|
| 21 | Hash Maps | Group Anagrams ([LC 49](https://leetcode.com/problems/group-anagrams/)) ⭐⭐ | Contains Duplicate ([LC 217](https://leetcode.com/problems/contains-duplicate/)) |
| 22 | Two Pointers | 3Sum ([LC 15](https://leetcode.com/problems/3sum/)) ⭐⭐ | Container With Most Water ([LC 11](https://leetcode.com/problems/container-with-most-water/)) ⭐⭐ |
| 23 | Sliding Window | Minimum Window Substring ([LC 76](https://leetcode.com/problems/minimum-window-substring/)) ⭐⭐ | Longest Repeating Char Replacement ([LC 424](https://leetcode.com/problems/longest-repeating-character-replacement/)) |
| 24 | Binary Search | Search Insert ([LC 35](https://leetcode.com/problems/search-insert-position/)) ⭐ | Find Min in Rotated Array ([LC 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)) ⭐⭐ |
| 25 | Linked Lists | Merge Two Sorted Lists ([LC 21](https://leetcode.com/problems/merge-two-sorted-lists/)) ⭐⭐ | LRU Cache ([LC 146](https://leetcode.com/problems/lru-cache/)) ⭐⭐ |
| 26 | Fast/Slow | Linked List Cycle II ([LC 142](https://leetcode.com/problems/linked-list-cycle-ii/)) | Remove Nth From End ([LC 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)) |
| 27 | Stacks | Min Stack ([LC 155](https://leetcode.com/problems/min-stack/)) | Evaluate RPN ([LC 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/)) |
| 28 | Prefix Sums | Product of Array Except Self ([LC 238](https://leetcode.com/problems/product-of-array-except-self/)) ⭐⭐ | Maximum Subarray ([LC 53](https://leetcode.com/problems/maximum-subarray/)) ⭐⭐ |
| 29 | Intervals | Insert Interval ([LC 57](https://leetcode.com/problems/insert-interval/)) | Non-overlapping Intervals ([LC 435](https://leetcode.com/problems/non-overlapping-intervals/)) |
| 30 | Trees | Invert Binary Tree ([LC 226](https://leetcode.com/problems/invert-binary-tree/)) ⭐⭐ | Binary Tree Max Path Sum ([LC 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/)) ⭐⭐ |
| 31 | Trees | Serialize/Deserialize BST ([LC 449](https://leetcode.com/problems/serialize-and-deserialize-bst/)) ⭐⭐ | Construct from Preorder/Inorder ([LC 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)) |
| 32 | Tries | Word Search II ([LC 212](https://leetcode.com/problems/word-search-ii/)) | — (re-solve [LC 208](https://leetcode.com/problems/implement-trie-prefix-tree/) from memory) |
| 33 | Graphs | Clone Graph ([LC 133](https://leetcode.com/problems/clone-graph/)) | Word Ladder ([LC 127](https://leetcode.com/problems/word-ladder/)) ⭐⭐ |
| 34 | Heaps | Merge K Sorted Lists ([LC 23](https://leetcode.com/problems/merge-k-sorted-lists/)) ⭐⭐ | Find Median from Data Stream ([LC 295](https://leetcode.com/problems/find-median-from-data-stream/)) ⭐⭐ |
| 35 | Greedy | Gas Station ([LC 134](https://leetcode.com/problems/gas-station/)) | Task Scheduler ([LC 621](https://leetcode.com/problems/task-scheduler/)) |
| 36 | Backtracking | Permutations ([LC 46](https://leetcode.com/problems/permutations/)) | Letter Combinations ([LC 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)) |
| 37 | DP | House Robber ([LC 198](https://leetcode.com/problems/house-robber/)) ⭐⭐ | Word Break ([LC 139](https://leetcode.com/problems/word-break/)) ⭐⭐ |
| 38 | DP | Longest Increasing Subsequence ([LC 300](https://leetcode.com/problems/longest-increasing-subsequence/)) ⭐⭐ | Decode Ways ([LC 91](https://leetcode.com/problems/decode-ways/)) |
| 39 | Sort & Search | Sort List ([LC 148](https://leetcode.com/problems/sort-list/)) | Koko Eating Bananas ([LC 875](https://leetcode.com/problems/koko-eating-bananas/)) |
| 40 | Bit & Math | Number of 1 Bits ([LC 191](https://leetcode.com/problems/number-of-1-bits/)) | Pow(x, n) ([LC 50](https://leetcode.com/problems/powx-n/)) |

**Pass 2 rest day (Day 41):** re-solve 4 problems from your weakest patterns (from Pass 1 rest day list).

**Pass 2 exit criteria:**
- [ ] ~76 total problems attempted
- [ ] LRU Cache, Min Window, Coin Change attempted
- [ ] Pattern recognition before coding on most problems

---

## Pass 3 — Polish & Interview Ready (~2–3 weeks)

**2 problems/day split:**
- **Problem 1:** new ⭐⭐ you haven't done, OR weak-pattern drill
- **Problem 2:** cold re-solve from memory (no notes)

### Week A — FAANG gaps (pick pairs)

| Day | Problem 1 | Problem 2 (re-solve) |
|---|---|---|
| A1 | Trapping Rain Water ([LC 42](https://leetcode.com/problems/trapping-rain-water/)) ⭐⭐ | Two Sum |
| A2 | Valid Parentheses ([LC 20](https://leetcode.com/problems/valid-parentheses/)) ⭐⭐ | Longest Substring |
| A3 | Rotting Oranges ([LC 994](https://leetcode.com/problems/rotting-oranges/)) | Merge Intervals |
| A4 | Binary Tree LCA ([LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)) | 3Sum |
| A5 | Merge K Sorted Lists ([LC 23](https://leetcode.com/problems/merge-k-sorted-lists/)) | Number of Islands |
| A6 | Word Break ([LC 139](https://leetcode.com/problems/word-break/)) | LRU Cache |
| A7 | Rest | Skim cheat sheet |

### Week B — Timed mocks

| Day | Activity |
|---|---|
| B1–B3 | Random ⭐⭐ Medium, 45 min timed, journal after |
| B4–B5 | Re-solve 2 worst mock problems |
| B6 | Mock + explain solution out loud |
| B7 | Light review only |

**Before interview:** only re-solves + cheat sheet. No new Hard problems.

---

## FAANG Must-Know (⭐⭐) — 31 problems

Use as Pass 3 checklist. All should be solvable from memory by interview day.

| # | Problem | LC | Pass |
|---|---|---|---|
| 1 | Two Sum | [1](https://leetcode.com/problems/two-sum/) | 1 |
| 2 | Valid Parentheses | [20](https://leetcode.com/problems/valid-parentheses/) | 2 |
| 3 | Longest Substring Without Repeating | [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 1 |
| 4 | Minimum Window Substring | [76](https://leetcode.com/problems/minimum-window-substring/) | 2 |
| 5 | 3Sum | [15](https://leetcode.com/problems/3sum/) | 2 |
| 6 | Container With Most Water | [11](https://leetcode.com/problems/container-with-most-water/) | 2 |
| 7 | Product of Array Except Self | [238](https://leetcode.com/problems/product-of-array-except-self/) | 2 |
| 8 | Merge Intervals | [56](https://leetcode.com/problems/merge-intervals/) | 1 |
| 9 | Meeting Rooms II | [253](https://leetcode.com/problems/meeting-rooms-ii/) | 1 |
| 10 | Binary Search | [704](https://leetcode.com/problems/binary-search/) | 1 ✓ |
| 11 | First & Last Position | [34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | 1 ✓ |
| 12 | Search Rotated Sorted Array | [33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 2 |
| 13 | Reverse Linked List | [206](https://leetcode.com/problems/reverse-linked-list/) | 1 |
| 14 | LRU Cache | [146](https://leetcode.com/problems/lru-cache/) | 2 |
| 15 | Number of Islands | [200](https://leetcode.com/problems/number-of-islands/) | 1 |
| 16 | Course Schedule | [207](https://leetcode.com/problems/course-schedule/) | 1 |
| 17 | Max Depth / Level Order | [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) / [102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | 1 |
| 18 | Validate BST | [98](https://leetcode.com/problems/validate-binary-search-tree/) | 1 |
| 19 | Lowest Common Ancestor | [236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | 1 |
| 20 | Kth Largest Element | [215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 1 |
| 21 | Top K Frequent Elements | [347](https://leetcode.com/problems/top-k-frequent-elements/) | 1 |
| 22 | Merge K Sorted Lists | [23](https://leetcode.com/problems/merge-k-sorted-lists/) | 2 |
| 23 | Subsets | [78](https://leetcode.com/problems/subsets/) | 1 |
| 24 | Combination Sum | [39](https://leetcode.com/problems/combination-sum/) | 1 |
| 25 | Climbing Stairs | [70](https://leetcode.com/problems/climbing-stairs/) | 1 |
| 26 | House Robber | [198](https://leetcode.com/problems/house-robber/) | 2 |
| 27 | Coin Change | [322](https://leetcode.com/problems/coin-change/) | 1 |
| 28 | Word Break | [139](https://leetcode.com/problems/word-break/) | 2 |
| 29 | Longest Increasing Subsequence | [300](https://leetcode.com/problems/longest-increasing-subsequence/) | 2 |
| 30 | Trapping Rain Water | [42](https://leetcode.com/problems/trapping-rain-water/) | 3 |
| 31 | Word Ladder | [127](https://leetcode.com/problems/word-ladder/) | 2 |

---

## Progress at a Glance

| Pass | Days | Problems | Status |
|---|---|---|---|
| **Pass 1** breadth | 1–20 | ~38 | **Day 1 done (today)** → Day 2 next |
| **Pass 2** depth | 21–41 | ~38 more | not started |
| **Pass 3** polish | ~14 | mocks + ⭐⭐ | not started |

**Total timeline at 2/day:** ~55 study days ≈ **8–11 weeks** (with rest days)

---

## Pattern Mastery Checklist

Mark when Pass 1 **and** Pass 2 are done for that pattern:

| Pattern | Pass 1 | Pass 2 | From memory |
|---|---|---|---|
| Hash Maps | [ ] | [ ] | [ ] |
| Two Pointer | [ ] | [ ] | [ ] |
| Sliding Window | [ ] | [ ] | [ ] |
| Binary Search | [x] | [ ] | [ ] |
| Linked List | [ ] | [ ] | [ ] |
| Fast/Slow | [ ] | [ ] | [ ] |
| Stacks | [ ] | [ ] | [ ] |
| Prefix Sums | [ ] | [ ] | [ ] |
| Intervals | [ ] | [ ] | [ ] |
| Trees | [ ] | [ ] | [ ] |
| Tries | [ ] | [ ] | [ ] |
| Graphs | [ ] | [ ] | [ ] |
| Heaps | [ ] | [ ] | [ ] |
| Greedy | [ ] | [ ] | [ ] |
| Backtracking | [ ] | [ ] | [ ] |
| DP | [ ] | [ ] | [ ] |
| Sort & Search | [ ] | [ ] | [ ] |
| Bit / Math | [ ] | [ ] | [ ] |

---

## Mistakes Journal

```
Date | Pass | Problem (LC) | Thought pattern / actual | Stuck where | Fix
```

| Date | Problem | Lesson |
|---|---|---|
| Jun 23 | [LC 704](https://leetcode.com/problems/binary-search/) | left<=right, mid±1 |
| Jun 23 | [LC 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | find_first → right=mid-1; find_last → left=mid+1 |
| | [LC 35](https://leetcode.com/problems/search-insert-position/) | not found → return `left` |

---

## Session Types (by energy)

| Energy | Do | Counts as |
|---|---|---|
| Normal | 2 new problems from current day | full day ✓ |
| Low | 1 new + 1 re-solve from yesterday | full day ✓ |
| Very low | 1 re-solve from memory only | half day — repeat tomorrow |

---

## Book Cross-Reference (optional)

| Pattern day | Book chapter |
|---|---|
| Day 1–2 | Ch 6, Ch 2 |
| Day 3 | Ch 1 |
| Day 4 | Ch 5 |
| Day 5–6 | Ch 3, Ch 4 |
| Day 7 | Ch 7 |
| Day 8 | Ch 10 |
| Day 9 | Ch 9 |
| Day 10–11 | Ch 11 |
| Day 12 | Ch 12 |
| Day 13 | Ch 13 |
| Day 14 | Ch 8 |
| Day 15 | Ch 16 |
| Day 16 | Ch 14 |
| Day 17 | Ch 15 |
| Day 18 | Ch 17 |
| Day 19 | Ch 18, Ch 19 |

---

## Resources

| File | Purpose |
|---|---|
| [INTERVIEW_PLAN.md](INTERVIEW_PLAN.md) | **This file — daily schedule** |
| [PROBLEM_SOLVING_GUIDE.md](PROBLEM_SOLVING_GUIDE.md) | How to think through problems |
| [README.md](README.md) | Vault solution index |
| Your book | Optional when a pattern feels unclear |

---

## Today — Pass 1 · Day 1 ✓ (Jun 23, 2026)

**Binary Search** — 2 problems done:

| Done | Problem | LC | Vault |
|---|---|---|---|
| [x] | Binary Search | [704](https://leetcode.com/problems/binary-search/) | [01_binary_search.py](binary-search/problems/01_binary_search.py) |
| [x] | Find First and Last Position | [34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [02_search_first_last.py](binary-search/problems/02_search_first_last.py) |

**Key takeaways:** standard template (704) · on match keep searching left/right (34) · `result` is a single int per helper.

---

## Tomorrow — Pass 1 · Day 2 (Hash Maps)

**Read first (10 min):** [hash-maps/notes.md](hash-maps/notes.md)

| # | Problem | LC | Tip |
|---|---|---|---|
| 1 | Two Sum | [1](https://leetcode.com/problems/two-sum/) | Plan in comments before coding. Check vault after. |
| 2 | Valid Anagram | [242](https://leetcode.com/problems/valid-anagram/) | Ask: hash map or sort? |

**After solving:** compare problem 1 with [01_two_sum.py](hash-maps/problems/01_two_sum.py).

---

*2 problems. Next pattern. Circle back later. That's the whole system.*
