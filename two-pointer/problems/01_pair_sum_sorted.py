"""
================================================================================
PROBLEM: Pair Sum in Sorted Array (Two Sum II)
================================================================================

QUESTION:
---------
Given a 1-indexed array of integers `numbers` that is already sorted in 
non-decreasing order, find two numbers such that they add up to a specific 
target number.

Return the indices of the two numbers (1-indexed) as an integer array [index1, index2].

You may not use the same element twice, and there is exactly one solution.

Example 1:
    Input: numbers = [2, 7, 11, 15], target = 9
    Output: [1, 2]
    Explanation: 2 + 7 = 9, indices are 1 and 2.

Example 2:
    Input: numbers = [2, 3, 4], target = 6
    Output: [1, 3]

Example 3:
    Input: numbers = [-1, 0], target = -1
    Output: [1, 2]

Constraints:
    - 2 <= numbers.length <= 3 * 10^4
    - -1000 <= numbers[i] <= 1000
    - numbers is sorted in non-decreasing order
    - -1000 <= target <= 1000
    - Only one valid answer exists

================================================================================
INTUITION:
================================================================================

Why Two Pointers Work Here:
---------------------------
1. SORTED ARRAY = PREDICTABLE DYNAMICS
   - If current sum is too small → move left pointer right (increases sum)
   - If current sum is too large → move right pointer left (decreases sum)

2. WHY START AT EXTREMES?
   - Left pointer at smallest value, right at largest
   - This gives us maximum control over sum adjustment
   - We can only increase (move left) or decrease (move right)

3. WHY NOT HASH MAP?
   - Hash map: O(n) time, O(n) space
   - Two pointers: O(n) time, O(1) space ← Better!
   - The sorted property is a "gift" - use it!

Visual Walkthrough:
-------------------
numbers = [2, 7, 11, 15], target = 9

Step 1: [2, 7, 11, 15]    sum = 2+15 = 17 > 9  → move R left
         L          R

Step 2: [2, 7, 11, 15]    sum = 2+11 = 13 > 9  → move R left
         L      R

Step 3: [2, 7, 11, 15]    sum = 2+7 = 9 == 9   → FOUND!
         L  R

================================================================================
IMPLEMENTATION:
================================================================================
"""

from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    Find two numbers in sorted array that sum to target.
    Returns 1-indexed positions.
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Convert to 1-indexed
        elif current_sum < target:
            left += 1   # Need larger sum → move left pointer right
        else:
            right -= 1  # Need smaller sum → move right pointer left
    
    return []  # No solution found (shouldn't happen per problem constraints)


def two_sum_sorted_0_indexed(numbers: List[int], target: int) -> List[int]:
    """
    Alternative: Returns 0-indexed positions (more common in practice).
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TIME COMPLEXITY: O(n)
- Each element is visited at most once
- Left pointer only moves right, right pointer only moves left
- Total movements ≤ n

SPACE COMPLEXITY: O(1)
- Only using two pointer variables
- No additional data structures

COMPARISON WITH ALTERNATIVES:
-----------------------------
| Approach      | Time    | Space   | Notes                          |
|---------------|---------|---------|--------------------------------|
| Brute Force   | O(n²)   | O(1)    | Check all pairs                |
| Hash Map      | O(n)    | O(n)    | Store complements              |
| Two Pointers  | O(n)    | O(1)    | Best! Uses sorted property     |
| Binary Search | O(nlogn)| O(1)    | For each element, search rest  |

================================================================================
INTERVIEW TIPS:
================================================================================

1. CLARIFYING QUESTIONS TO ASK:
   - "Is the array sorted?" (Critical for this approach!)
   - "Are there duplicates?"
   - "Is there guaranteed to be exactly one solution?"
   - "What should I return if no solution exists?"
   - "Is it 0-indexed or 1-indexed?"

2. EDGE CASES TO MENTION:
   - Minimum array size (2 elements)
   - Negative numbers
   - Target is 0 (need positive + negative or two zeros)
   - All same elements

3. OPTIMIZATION TALKING POINTS:
   - "Since the array is sorted, I can use two pointers instead of a hash map"
   - "This reduces space complexity from O(n) to O(1)"
   - "The sorted property gives us predictable behavior when adjusting pointers"

4. COMMON MISTAKES:
   - Using hash map when array is sorted (wastes the "gift")
   - Off-by-one error with 1-indexed output
   - Forgetting to move pointers (infinite loop)

5. FOLLOW-UP QUESTIONS:
   - "What if array is unsorted?" → Sort first O(nlogn) or use hash map
   - "What if there are multiple solutions?" → Return all pairs
   - "What if we want three numbers?" → Three Sum problem

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        # (numbers, target, expected)
        ([2, 7, 11, 15], 9, [1, 2]),           # Basic case
        ([2, 3, 4], 6, [1, 3]),                 # Target at extremes
        ([-1, 0], -1, [1, 2]),                  # Negative numbers
        ([1, 2, 3, 4, 5], 9, [4, 5]),           # Solution at end
        ([1, 2, 3, 4, 5], 3, [1, 2]),           # Solution at start
        ([0, 0, 3, 4], 0, [1, 2]),              # Zero sum with duplicates
        ([-3, -1, 0, 1, 2], -4, [1, 2]),        # Negative target
        ([1, 3, 5, 7, 9, 11], 16, [3, 6]),      # Mid-array solution
    ]
    
    print("=" * 60)
    print("PAIR SUM SORTED - TEST RESULTS")
    print("=" * 60)
    
    all_passed = True
    for i, (numbers, target, expected) in enumerate(test_cases, 1):
        result = two_sum_sorted(numbers, target)
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:    numbers={numbers}, target={target}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {'All tests passed!' if all_passed else 'Some tests failed.'}")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()

