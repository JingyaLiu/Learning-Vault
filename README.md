# Learning-Vault

A pattern-based coding interview prep vault. Each folder covers one algorithmic pattern with study notes and worked Python solutions.

---

## How to Use This Vault

1. **Read `PROBLEM_SOLVING_GUIDE.md` first** — it gives you a repeatable thinking process for any problem you face.
2. Pick a pattern folder and read the `notes.md` to understand the concept.
3. Try a problem from the practice list in the notes *before* reading the solution.
4. Read the solution file — pay attention to the **INTUITION** section, not just the code.
5. Re-solve it from memory the next day.

---

## Patterns

| Folder | Notes | Problems | Status |
|---|---|---|---|
| [`two-pointer/`](two-pointer/) | [notes.md](two-pointer/notes.md) | 4 | Complete |
| [`hash-maps/`](hash-maps/) | [notes.md](hash-maps/notes.md) | 3 | Complete |
| [`sliding-windows/`](sliding-windows/) | [notes.md](sliding-windows/notes.md) | 2 | Complete |
| [`binary-search/`](binary-search/) | [notes.md](binary-search/notes.md) | 0 | Notes only |
| [`fast-slow-pointer/`](fast-slow-pointer/) | [notes.md](fast-slow-pointer/notes.md) | 0 | Notes only |
| [`linked-list/`](linked-list/) | [notes.md](linked-list/notes.md) | 0 | Notes only |

---

## Solutions Index

### Two Pointer
| File | Problem | Difficulty |
|---|---|---|
| [01_pair_sum_sorted.py](two-pointer/problems/01_pair_sum_sorted.py) | Two Sum II | Easy |
| [02_triplet_sum.py](two-pointer/problems/02_triplet_sum.py) | 3Sum | Medium |
| [03_valid_palindrome.py](two-pointer/problems/03_valid_palindrome.py) | Valid Palindrome | Easy |
| [04_container_with_most_water.py](two-pointer/problems/04_container_with_most_water.py) | Container With Most Water | Medium |

### Hash Maps
| File | Problem | Difficulty |
|---|---|---|
| [01_two_sum.py](hash-maps/problems/01_two_sum.py) | Two Sum | Easy |
| [02_valid_sudoku.py](hash-maps/problems/02_valid_sudoku.py) | Valid Sudoku | Medium |
| [03_set_matrix_zeroes.py](hash-maps/problems/03_set_matrix_zeroes.py) | Set Matrix Zeroes | Medium |

### Sliding Window
| File | Problem | Difficulty |
|---|---|---|
| [longest_substring_unique_3.py](sliding-windows/problems/longest_substring_unique_3.py) | Longest Substring Without Repeating Characters (LC 3) | Medium |
| [find_anagrams_in_string_438.py](sliding-windows/problems/find_anagrams_in_string_438.py) | Find All Anagrams in a String (LC 438) | Medium |

---

## Running a Solution

Each solution file is self-contained and has its own test runner:

```bash
python3 two-pointer/problems/01_pair_sum_sorted.py
python3 sliding-windows/problems/longest_substring_unique_3.py
```

---

## Key Reference

**Stuck on a problem?** → Read [`PROBLEM_SOLVING_GUIDE.md`](PROBLEM_SOLVING_GUIDE.md)
