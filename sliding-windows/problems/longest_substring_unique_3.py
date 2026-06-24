"""
================================================================================
PROBLEM: Longest Substring Without Repeating Characters (LeetCode 3)
================================================================================

QUESTION:
---------
Given a string `s`, find the length of the longest substring without repeating
characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with length 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with length 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with length 3. "pwke" is a subsequence,
    not a substring.

Constraints:
    - 0 <= s.length <= 5 * 10^4
    - s consists of English letters, digits, symbols and spaces.

================================================================================
INTUITION:
================================================================================

Why Dynamic Sliding Window Works Here:
--------------------------------------
1. SUBSTRING = CONTIGUOUS
   - We care about a contiguous segment [left, right]
   - "No repeating" means every char in the window appears exactly once

2. DYNAMIC WINDOW
   - Expand: move right to include new characters
   - Shrink: when s[right] is already in the window, move left past its previous
     occurrence so the window has no duplicate again

3. TRACK LAST SEEN INDEX
   - Use a map char -> last index. When we see a repeat, set left = max(left,
     last_seen[s[right]] + 1) so the window [left, right] has no duplicate.
   - This keeps the window valid in O(1) per step → O(n) total.

Visual Walkthrough (s = "abcabcbb"):
-----------------------------------
right=0 'a': seen={a:0}, left=0, len=1
right=1 'b': seen={a:0,b:1}, len=2
right=2 'c': seen={a:0,b:1,c:2}, len=3  ← max so far
right=3 'a': duplicate! left = max(0, 0+1)=1, seen={a:3,b:1,c:2}, len=3
right=4 'b': duplicate! left = max(1, 1+1)=2, seen={a:3,b:4,c:2}, len=3
...

================================================================================
BUGS IN THE ORIGINAL APPROACH:
================================================================================

1. OFF-BY-ONE IN WINDOW
   - Original used s[left:right] (excludes index right) but then set
     max_len = (right - left + 1). So it measured length including right
     without checking whether s[right] is already in the window.
   - Fix: Either check s[left:right+1] for uniqueness, or (better) track
     chars in the window and decide validity after including s[right].

2. SHRINK BY ONLY ONE
   - On duplicate, original did left += 1 once. The window might still
     contain the duplicate (e.g. "abca" -> left=1 gives "bca" but we're
     at right=3; next we'll add right=4. So we need to shrink until
     the window is valid.
   - Fix: Either loop "while invalid: left += 1", or use last-seen index:
     left = last_seen[s[right]] + 1.

3. O(n^2) PER CHECK
   - set(s[left:right]) and len(s[left:right]) are O(window size) each time.
   - Fix: Maintain a dict/set and update in O(1) when we add/remove a char
     (or use last-seen map and no explicit remove).

================================================================================
IMPLEMENTATION:
================================================================================
"""


def length_of_longest_substring(s: str) -> int:
    """
    Longest substring with all unique characters using dynamic sliding window.
    Track last index of each char; when we see a repeat, jump left past it.
    Time: O(n), Space: O(min(n, alphabet)).
    """
    last_seen = {}  # char -> latest index in current window context
    left = 0
    max_len = 0

    for right, c in enumerate(s):
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1
        last_seen[c] = right
        max_len = max(max_len, right - left + 1)

    return max_len


def length_of_longest_substring_set(s: str) -> int:
    """
    Same idea using a set for the current window: expand right, shrink left
    until the window has no duplicate. O(n) time, O(min(n, alphabet)) space.
    """
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.discard(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


class Solution:
    """LeetCode-style wrapper."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        return length_of_longest_substring(s)


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TIME COMPLEXITY: O(n)
- Each index is visited at most twice (right advances n times; left only moves
  forward and never back).

SPACE COMPLEXITY: O(min(n, |alphabet|))
- We store at most one index per distinct character in the string.

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("abba", 2),
    ]

    print("=" * 60)
    print("LONGEST SUBSTRING WITHOUT REPEATING - TEST RESULTS")
    print("=" * 60)

    all_passed = True
    for i, (s, expected) in enumerate(test_cases, 1):
        result = length_of_longest_substring(s)
        passed = result == expected
        all_passed = all_passed and passed

        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:    s={s!r}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")

    print("\n" + "=" * 60)
    print(f"SUMMARY: {'All tests passed!' if all_passed else 'Some tests failed.'}")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
