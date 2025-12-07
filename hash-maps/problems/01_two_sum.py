"""
================================================================================
PROBLEM: Two Sum
================================================================================

QUESTION:
---------
Given an array of integers `nums` and an integer `target`, return indices of the 
two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]

Example 3:
    Input: nums = [3, 3], target = 6
    Output: [0, 1]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.

================================================================================
INTUITION:
================================================================================

Why Hash Map Works Here:
------------------------
1. FAST LOOKUP NEEDED
   - For each number, we need to check if its complement (target - num) exists
   - Hash map provides O(1) average lookup time
   - Without hash map: O(n) lookup per element = O(n²) total

2. ONE-PASS SOLUTION
   - We can build the hash map as we iterate
   - Check if complement exists before adding current number
   - This ensures we don't use the same element twice

3. WHY NOT SORTING?
   - Sorting would be O(nlogn) time
   - We'd lose original indices (need to track them)
   - Hash map: O(n) time, O(n) space ← Better for unsorted!

Visual Walkthrough:
-------------------
nums = [2, 7, 11, 15], target = 9

Step 1: num = 2, complement = 9 - 2 = 7
        seen = {} → 7 not found, add {2: 0}
        seen = {2: 0}

Step 2: num = 7, complement = 9 - 7 = 2
        seen = {2: 0} → 2 found! Return [0, 1]
        ✓ FOUND!

Alternative walkthrough:
nums = [3, 2, 4], target = 6

Step 1: num = 3, complement = 6 - 3 = 3
        seen = {} → 3 not found, add {3: 0}
        seen = {3: 0}

Step 2: num = 2, complement = 6 - 2 = 4
        seen = {3: 0} → 4 not found, add {3: 0, 2: 1}
        seen = {3: 0, 2: 1}

Step 3: num = 4, complement = 6 - 4 = 2
        seen = {3: 0, 2: 1} → 2 found! Return [1, 2]
        ✓ FOUND!

================================================================================
IMPLEMENTATION:
================================================================================
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that sum to target using hash map.
    Returns 0-indexed positions.
    """
    seen = {}  # Maps number -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in seen
        if complement in seen:
            return [seen[complement], i]
        
        # Add current number to seen (after checking to avoid using same element)
        seen[num] = i
    
    return []  # No solution found (shouldn't happen per problem constraints)


def two_sum_alternative(nums: List[int], target: int) -> List[int]:
    """
    Alternative implementation using .get() method.
    Uses .get() with None default to check existence.
    Functionally identical to two_sum(), just different style.
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # .get() returns None if key doesn't exist
        complement_index = seen.get(complement)
        if complement_index is not None:
            return [complement_index, i]
        
        seen[num] = i
    
    return []


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach for comparison.
    Time: O(n²), Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TIME COMPLEXITY: O(n)
- Single pass through the array
- Hash map operations (insert, lookup) are O(1) average case
- Total: O(n) * O(1) = O(n)

SPACE COMPLEXITY: O(n)
- Hash map stores at most n-1 elements (worst case)
- In worst case, we store all elements except the last one

COMPARISON WITH ALTERNATIVES:
-----------------------------
| Approach      | Time    | Space   | Notes                          |
|---------------|---------|---------|--------------------------------|
| Brute Force   | O(n²)   | O(1)    | Check all pairs                |
| Hash Map      | O(n)    | O(n)    | Best! Fast lookup              |
| Sorting + TP  | O(nlogn)| O(1)    | If we don't need indices       |
| Two Pass      | O(n)    | O(n)    | Build map first, then search   |

Note: Two-pass approach builds the entire hash map first, then searches.
One-pass is more elegant and has same complexity.

================================================================================
INTERVIEW TIPS:
================================================================================

1. CLARIFYING QUESTIONS TO ASK:
   - "Can the array contain duplicates?" (Yes, but can't use same index twice)
   - "Are there negative numbers?" (Yes, handle normally)
   - "Is there guaranteed to be exactly one solution?"
   - "What should I return if no solution exists?"
   - "Can I use the same element twice?" (No, different indices)

2. EDGE CASES TO MENTION:
   - Minimum array size (2 elements)
   - Negative numbers and negative target
   - Zero as target (need positive + negative or two zeros)
   - Duplicate numbers (e.g., [3, 3], target = 6)
   - Large numbers (overflow considerations)

3. OPTIMIZATION TALKING POINTS:
   - "I'll use a hash map for O(1) complement lookup"
   - "One-pass solution: build map as we go"
   - "This avoids using the same element twice by checking before adding"
   - "Trade-off: O(n) space for O(n) time vs O(n²) time"

4. COMMON MISTAKES:
   - Adding to hash map before checking complement (might use same element)
   - Using same index twice (check complement first!)
   - Forgetting to handle case when no solution exists
   - Off-by-one errors in index tracking

5. FOLLOW-UP QUESTIONS:
   - "What if array is sorted?" → Use two pointers (O(1) space)
   - "What if there are multiple solutions?" → Return all pairs
   - "What if we want three numbers?" → Three Sum problem
   - "What if we want all pairs (not just indices)?" → Return values
   - "What if we can't use extra space?" → Sort + two pointers (but lose indices)

6. WHY HASH MAP OVER OTHER APPROACHES:
   - vs Brute Force: O(n) vs O(n²) time
   - vs Sorting: Preserves original indices, simpler code
   - vs Two Pointers: Works on unsorted arrays

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        # (nums, target, expected)
        ([2, 7, 11, 15], 9, [0, 1]),              # Basic case
        ([3, 2, 4], 6, [1, 2]),                    # Not at start
        ([3, 3], 6, [0, 1]),                       # Duplicates
        ([1, 2, 3, 4, 5], 9, [3, 4]),             # Solution at end
        ([1, 2, 3, 4, 5], 3, [0, 1]),             # Solution at start
        ([0, 0, 3, 4], 0, [0, 1]),                # Zero sum with duplicates
        ([-3, -1, 0, 1, 2], -4, [0, 1]),          # Negative target
        ([1, 5, 3, 7, 9, 11], 16, [3, 4]),        # Unsorted array
        ([-1, -2, -3, -4, -5], -8, [2, 4]),       # All negatives
        ([10, 20, 30, 40, 50], 60, [1, 3]),       # Larger numbers
    ]
    
    print("=" * 60)
    print("TWO SUM - TEST RESULTS")
    print("=" * 60)
    
    all_passed = True
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = two_sum(nums, target)
        # Sort results for comparison (order doesn't matter)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        passed = result_sorted == expected_sorted
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

