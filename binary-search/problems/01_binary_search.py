"""
================================================================================
PROBLEM: Binary Search (LeetCode 704)
================================================================================

QUESTION:
---------
Given an array of integers `nums` which is sorted in ascending order, and an
integer `target`, write a function to search `target` in `nums`. If `target`
exists, return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4

Example 2:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
    Output: -1

Constraints:
    - 1 <= nums.length <= 10^4
    - -10^4 < nums[i], target < 10^4
    - All integers in nums are unique
    - nums is sorted in ascending order

================================================================================
INTUITION:
================================================================================

Why Binary Search Works Here:
-----------------------------
1. SORTED ARRAY = ELIMINATE HALF EACH STEP
   - Compare target with middle element
   - If target is smaller → it can only be in the left half
   - If target is larger → it can only be in the right half
   - Discard the half that cannot contain the answer

2. WHY O(log n)?
   - Each step cuts the search space in half
   - For n = 10,000 → at most ~14 comparisons (vs 10,000 for linear search)

3. THE THREE MOVES (memorize these)
   - target == nums[mid]  → found, return mid
   - target <  nums[mid]  → search left:  right = mid - 1
   - target >  nums[mid]  → search right: left  = mid + 1

Visual Walkthrough (nums = [-1, 0, 3, 5, 9, 12], target = 9):
----------------------------------------------------------------
Step 1: [-1,  0,  3,  5,  9, 12]   mid=3, nums[3]=5,  9>5 → go right
         L        M            R

Step 2: [-1,  0,  3,  5,  9, 12]   mid=4, nums[4]=9,  9==9 → FOUND at index 4
                     L  M     R

Visual Walkthrough (target = 2, not found):
--------------------------------------------
Step 1: mid=3, nums[3]=5,  2<5 → go left
Step 2: mid=1, nums[1]=0,  2>0 → go right
Step 3: mid=2, nums[2]=3,  2<3 → go left
Step 4: left > right → not found, return -1

================================================================================
IMPLEMENTATION:
================================================================================
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Standard binary search: find exact index of target, or -1 if absent.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


class Solution:
    """LeetCode-style wrapper."""

    def search(self, nums: List[int], target: int) -> int:
        return search(nums, target)


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TIME COMPLEXITY: O(log n)
- Each iteration eliminates half the remaining search space.

SPACE COMPLEXITY: O(1)
- Only three pointers: left, right, mid.

================================================================================
INTERVIEW TIPS:
================================================================================

Clarifying questions:
- Is the array sorted? (yes, given)
- Are there duplicates? (this problem: no — simplifies to exact match)
- What to return if not found? (-1)

Edge cases:
- Single element array: [5], target=5 → 0; target=3 → -1
- Target at first index: nums[0]
- Target at last index: nums[-1]
- Target not in array at all

Why left <= right (not left < right)?
- We need to check the case when left == right (one element left)
- With left < right, a single-element window would be skipped

Why mid + 1 and mid - 1 (not mid)?
- We already checked nums[mid], so exclude it from the next search space
- Prevents infinite loops

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([2, 5], 5, 1),
        ([2, 5], 2, 0),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
    ]

    print("=" * 60)
    print("BINARY SEARCH (LC 704) - TEST RESULTS")
    print("=" * 60)

    all_passed = True
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = search(nums, target)
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
