"""
================================================================================
PROBLEM: Find All Anagrams in a String (LeetCode 438)
================================================================================

QUESTION:
---------
Given two strings `s` and `p`, return an array of all the start indices of `p`'s
anagrams in `s`. You may return the answer in any order.

An anagram is a string with the same characters and frequencies as another string.

Example 1:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0, 6]
    Explanation: "cba" at 0 and "bac" at 6 are anagrams of "abc".

Example 2:
    Input: s = "abab", p = "ab"
    Output: [0, 1, 2]
    Explanation: "ab", "ba", "ab" at 0, 1, 2 are anagrams of "ab".

Constraints:
    - 1 <= s.length, p.length <= 3 * 10^4
    - s and p consist of lowercase English letters.

================================================================================
INTUITION:
================================================================================

Why Fixed Sliding Window Works Here:
------------------------------------
1. ANAGRAM = SAME FREQUENCY OF CHARS
   - Compare window [i .. i+len(p)-1] with p using char counts
   - Two strings are anagrams iff their 26-letter frequency arrays match

2. FIXED WINDOW SIZE = len(p)
   - Each valid window has exactly len(p) characters
   - Slide by one: drop leftmost char, add next char on the right
   - Update frequency for the outgoing and incoming character only

3. WHY NOT CHECK EVERY SUBSTRING FROM SCRATCH?
   - Naive: O(n * len(p)) for n windows, each costing O(len(p)) to build counts
   - Sliding window: O(n) — each char enters and leaves the window at most once
   - Reuse the previous window’s counts instead of recomputing

Visual Walkthrough:
-------------------
s = "cbaebabacd", p = "abc"  (p_count = {a:1, b:1, c:1})

Step 1: window "cba" [0..2]  → s_count matches p_count → append 0
Step 2: window "bae" [1..3]   → 'e' in, 'c' out → no match
Step 3: window "aeb" [2..4]  → no match
...
Step 7: window "bac" [6..8]  → s_count matches p_count → append 6

================================================================================
IMPLEMENTATION:
================================================================================
"""

from typing import List


def find_anagrams(s: str, p: str) -> List[int]:
    """
    Find all start indices of anagrams of p in s using a fixed-length sliding window.
    Time: O(n), Space: O(1) — at most 26 counters.
    """
    if len(p) > len(s):
        return []

    p_count = [0] * 26
    for c in p:
        p_count[ord(c) - ord("a")] += 1

    # Build count for the first window s[0 : len(p)]
    window_count = [0] * 26
    for i in range(len(p)):
        window_count[ord(s[i]) - ord("a")] += 1

    result = []
    if window_count == p_count:
        result.append(0)

    # Slide the window: drop s[left], add s[right]
    left = 0
    for right in range(len(p), len(s)):
        window_count[ord(s[left]) - ord("a")] -= 1
        window_count[ord(s[right]) - ord("a")] += 1
        left += 1
        if window_count == p_count:
            result.append(left)

    return result


def find_anagrams_single_loop(s: str, p: str) -> List[int]:
    """
    Same idea with one loop: expand right, then shrink when window size equals len(p).
    """
    if len(p) > len(s):
        return []

    p_count = [0] * 26
    for c in p:
        p_count[ord(c) - ord("a")] += 1

    window_count = [0] * 26
    left = 0
    result = []

    for right in range(len(s)):
        window_count[ord(s[right]) - ord("a")] += 1

        if right - left + 1 == len(p):
            if window_count == p_count:
                result.append(left)
            window_count[ord(s[left]) - ord("a")] -= 1
            left += 1

    return result


class Solution:
    """LeetCode-style wrapper."""

    def findAnagrams(self, s: str, p: str) -> List[int]:
        return find_anagrams(s, p)


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TIME COMPLEXITY: O(n)
- One pass over s; each character added once and removed once from the window
- Comparing two length-26 lists is O(1)

SPACE COMPLEXITY: O(1)
- Two fixed arrays of size 26 (lowercase letters only)

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("aa", "bb", []),
        ("a", "a", [0]),
        ("aaaaaaaaaa", "aaaaaaaaaaaaa", []),
        ("af", "be", []),
    ]

    print("=" * 60)
    print("FIND ALL ANAGRAMS IN A STRING - TEST RESULTS")
    print("=" * 60)

    all_passed = True
    for i, (s, p, expected) in enumerate(test_cases, 1):
        result = find_anagrams(s, p)
        passed = result == expected
        all_passed = all_passed and passed

        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:    s={s!r}, p={p!r}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")

    print("\n" + "=" * 60)
    print(f"SUMMARY: {'All tests passed!' if all_passed else 'Some tests failed.'}")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
