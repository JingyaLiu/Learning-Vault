"""
================================================================================
PROBLEM: Find First and Last Position of Element in Sorted Array (LeetCode 34)
================================================================================

QUESTION:
---------
Given an array of integers `nums` sorted in non-decreasing order, find the
starting and ending position of a given `target` value.

If `target` is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [5, 7, 7, 8, 8, 10], target = 8
    Output: [3, 4]

Example 2:
    Input: nums = [5, 7, 7, 8, 8, 10], target = 6
    Output: [-1, -1]

Example 3:
    Input: nums = [], target = 0
    Output: [-1, -1]

Constraints:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i], target <= 10^9
    - nums is a non-decreasing array

================================================================================
INTUITION:
================================================================================

Why Two Binary Searches?
------------------------
Standard binary search stops at the first match. With duplicates, one match
is not enough — we need the leftmost and rightmost positions.

Run binary search twice:
1. find_first — on match, save mid and keep searching LEFT  (right = mid - 1)
2. find_last  — on match, save mid and keep searching RIGHT (left  = mid + 1)

Each helper returns a single index (or -1). Combine at the end → [first, last].

Visual Walkthrough (nums = [5, 7, 7, 8, 8, 10], target = 8):
---------------------------------------------------------------
find_first:
  mid=2, nums[2]=7  → too small → left=3
  mid=4, nums[4]=8  → found! result=4, right=3  (search left)
  mid=3, nums[3]=8  → found! result=3, right=2  (search left)
  left=3, right=2   → done, first=3

find_last:
  mid=2, nums[2]=7  → too small → left=3
  mid=4, nums[4]=8  → found! result=4, left=5   (search right)
  mid=5, nums[5]=10 → too big  → right=4
  left=5, right=4   → done, last=4

Answer: [3, 4]

Key difference on match:
  find_first: result = mid, right = mid - 1
  find_last:  result = mid, left  = mid + 1

================================================================================
IMPLEMENTATION:
================================================================================
"""

from typing import List


def find_first(nums: List[int], target: int) -> int:
    """TODO: cold re-solve — leftmost index of target, or -1."""
    raise NotImplementedError


def find_last(nums: List[int], target: int) -> int:
    """TODO: cold re-solve — rightmost index of target, or -1."""
    raise NotImplementedError


def search_range(nums: List[int], target: int) -> List[int]:
    """TODO: combine find_first + find_last."""
    raise NotImplementedError


class Solution:
    """LeetCode-style wrapper."""

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return search_range(nums, target)


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TIME COMPLEXITY: O(log n)
- Two independent binary searches, each O(log n).

SPACE COMPLEXITY: O(1)
- Only pointer variables; no extra data structures.

================================================================================
INTERVIEW TIPS:
================================================================================

Clarifying questions:
- Are there duplicates? (yes — that's why we need two searches)
- What if target is not found? (return [-1, -1])
- Can nums be empty? (yes)

Edge cases:
- Empty array → [-1, -1]
- Target not in array → [-1, -1]
- Single element that matches → [0, 0]
- All elements are target → [0, len(nums) - 1]

Why result = -1 (single int, not a list)?
- Each helper finds ONE index. The list [first, last] is built only when
  combining both results in search_range().

Why right = mid - 1 (not right -= 1)?
- Binary search must halve the search space. right -= 1 only moves by one
  step and breaks O(log n) behavior.

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([1], 0, [-1, -1]),
        ([2, 2], 2, [0, 1]),
        ([1, 2, 3], 2, [1, 1]),
        ([1, 1, 1, 1, 1], 1, [0, 4]),
    ]

    print("=" * 60)
    print("FIND FIRST AND LAST POSITION (LC 34) - TEST RESULTS")
    print("=" * 60)

    all_passed = True
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = search_range(nums, target)
        passed = result == expected
        all_passed = all_passed and passed

        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:    nums={nums}, target={target}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")

    print("\n" + "=" * 60)
    print(f"SUMMARY: {'All tests passed!' if all_passed else 'Some tests failed.'}")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
