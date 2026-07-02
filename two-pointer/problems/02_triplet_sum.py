"""
================================================================================
PROBLEM: Three Sum (Triplet Sum)
================================================================================

QUESTION:
---------
Given an integer array `nums`, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    Explanation:
        nums[0] + nums[1] + nums[2] = -1 + 0 + 1 = 0
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
        nums[0] + nums[3] + nums[4] = -1 + 2 + (-1) = 0
        The distinct triplets are [-1, 0, 1] and [-1, -1, 2].

Example 2:
    Input: nums = [0, 1, 1]
    Output: []

Example 3:
    Input: nums = [0, 0, 0]
    Output: [[0, 0, 0]]

Constraints:
    - 3 <= nums.length <= 3000
    - -10^5 <= nums[i] <= 10^5

================================================================================
INTUITION:
================================================================================

Key Insight: REDUCE 3SUM TO 2SUM
--------------------------------
For each element nums[i], we need to find two other elements that sum to -nums[i].
This transforms the problem into multiple Two Sum problems!

Strategy: STAGED TRAVERSAL
--------------------------
1. Sort the array (enables two-pointer technique)
2. Fix one pointer (i) - iterate through array
3. Use two pointers (left, right) on remaining subarray to find pair

Why Sorting?
------------
- Enables O(n) two-pointer search for each fixed element
- Makes duplicate handling easy (skip consecutive same values)
- Total: O(n²) instead of O(n³) brute force

Handling Duplicates:
-------------------
- Skip duplicate values for the fixed pointer
- Skip duplicate values when moving left/right pointers after finding a triplet

Visual Walkthrough:
-------------------
nums = [-1, 0, 1, 2, -1, -4]
After sorting: [-4, -1, -1, 0, 1, 2]

Iteration 1: Fix i=0 (-4), find pair summing to 4
[-4, -1, -1, 0, 1, 2]
  i   L            R     → -1 + 2 = 1 < 4, move L
  i       L        R     → -1 + 2 = 1 < 4, move L
  i          L     R     → 0 + 2 = 2 < 4, move L
  i             L  R     → 1 + 2 = 3 < 4, move L
  (L crosses R, no triplet found)

Iteration 2: Fix i=1 (-1), find pair summing to 1
[-4, -1, -1, 0, 1, 2]
      i   L        R     → -1 + 2 = 1 == 1, FOUND [-1, -1, 2]!
      i      L  R        → 0 + 1 = 1 == 1, FOUND [-1, 0, 1]!

Iteration 3: Skip i=2 (-1) - duplicate of i=1

================================================================================
IMPLEMENTATION:
================================================================================
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """TODO: cold re-solve — all unique triplets summing to 0."""

    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        target = -nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return result


def three_sum_with_target(nums: List[int], target: int) -> List[List[int]]:
    """
    Variation: Find triplets summing to a specific target.
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        remaining = target - nums[i]
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == remaining:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < remaining:
                left += 1
            else:
                right -= 1
    
    return result


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TIME COMPLEXITY: O(n²)
- Sorting: O(n log n)
- Outer loop: O(n) iterations
- Inner two-pointer search: O(n) for each iteration
- Total: O(n log n) + O(n × n) = O(n²)

SPACE COMPLEXITY: O(1) or O(n)
- O(1) extra space for pointers (excluding output)
- O(n) for sorting (depends on implementation)
- Output space not counted in space complexity

COMPARISON WITH ALTERNATIVES:
-----------------------------
| Approach          | Time     | Space  | Notes                         |
|-------------------|----------|--------|-------------------------------|
| Brute Force       | O(n³)    | O(1)   | Check all triplets            |
| Hash Map + Loop   | O(n²)    | O(n)   | For each pair, look up third  |
| Sort + Two Ptr    | O(n²)    | O(1)   | Best! Clean duplicate handling|

================================================================================
INTERVIEW TIPS:
================================================================================

1. CLARIFYING QUESTIONS TO ASK:
   - "Should the output contain unique triplets only?"
   - "Can the same element be used multiple times?"
   - "What if there are no valid triplets?"
   - "Does the order of elements in each triplet matter?"
   - "Does the order of triplets in the result matter?"

2. EDGE CASES TO MENTION:
   - Array with less than 3 elements → []
   - All zeros → [[0, 0, 0]]
   - All positive numbers → [] (can't sum to 0)
   - All negative numbers → [] (can't sum to 0)
   - Many duplicates → proper deduplication needed

3. OPTIMIZATION TALKING POINTS:
   - "Sorting enables efficient two-pointer search"
   - "Skip duplicates to avoid redundant work and duplicate results"
   - "Early termination when nums[i] > 0 (for target = 0)"

4. COMMON MISTAKES:
   - Forgetting to handle duplicates → duplicate triplets in result
   - Not moving BOTH pointers after finding triplet → infinite loop
   - Starting left at 0 instead of i+1 → using same element twice
   - Wrong duplicate skip (before vs after increment)

5. STEP-BY-STEP EXPLANATION:
   - "First, I'll sort to enable two-pointer technique"
   - "For each element, I reduce the problem to Two Sum"
   - "I skip duplicates at three levels: fixed pointer, left, and right"

6. FOLLOW-UP QUESTIONS:
   - "4Sum?" → Add another loop, O(n³)
   - "kSum?" → Recursion, reduce to (k-1)Sum
   - "Closest sum to target?" → Track minimum difference

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        # (nums, expected)
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),                                      # No solution
        ([0, 0, 0], [[0, 0, 0]]),                              # All zeros
        ([0, 0, 0, 0], [[0, 0, 0]]),                           # Multiple zeros
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),         # Multiple solutions
        ([1, 2, 3], []),                                       # All positive
        ([-3, -2, -1], []),                                    # All negative
        ([-1, -1, -1, 2], [[-1, -1, 2]]),                     # Duplicates
        ([-4, -2, -1, 0, 1, 2, 3], [[-4, 1, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
    ]
    
    print("=" * 60)
    print("THREE SUM - TEST RESULTS")
    print("=" * 60)
    
    all_passed = True
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = three_sum(nums.copy())  # Copy to preserve original
        
        # Sort both for comparison (order doesn't matter)
        result_sorted = sorted([sorted(x) for x in result])
        expected_sorted = sorted([sorted(x) for x in expected])
        
        passed = result_sorted == expected_sorted
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:    nums={nums}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {'All tests passed!' if all_passed else 'Some tests failed.'}")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()

