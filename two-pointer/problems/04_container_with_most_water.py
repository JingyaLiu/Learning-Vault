"""
================================================================================
PROBLEM: Container With Most Water (Largest Container)
================================================================================

QUESTION:
---------
You are given an integer array `height` of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container holds the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: Lines at index 1 (height=8) and index 8 (height=7)
                 form a container with area = min(8,7) × (8-1) = 7 × 7 = 49

         8   |       |
         7   |       |   |
         6   |   |   |   |
         5   |   |   |   |
         4   |   |   | | |
         3   |   |   | | | |
         2   |   | | | | | |
         1 | |   | | | | | |
           0 1 2 3 4 5 6 7 8

Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    - n == height.length
    - 2 <= n <= 10^5
    - 0 <= height[i] <= 10^4

================================================================================
INTUITION:
================================================================================

Key Formula:
------------
Area = min(height[left], height[right]) × (right - left)
       ↑ limited by shorter line       ↑ width

Why Two Pointers? OPTIMAL SUBSTRUCTURE
--------------------------------------
1. Start with MAXIMUM WIDTH (pointers at both ends)
2. To potentially find larger area, we MUST increase height
3. Moving the shorter line might find a taller one
4. Moving the taller line can NEVER increase area (width decreases, height limited by shorter)

The Greedy Choice:
-----------------
- Always move the pointer at the SHORTER line
- This is the only way to potentially increase the limiting factor (height)
- Width will always decrease, so we need taller lines to compensate

Why This Works (Proof Intuition):
---------------------------------
If height[left] < height[right]:
  - Current area = height[left] × width
  - Moving right pointer: new_area ≤ height[left] × (width-1) < current area
  - Moving left pointer: might find taller line → might increase area
  
So moving the shorter pointer is the only option that could improve.

Visual Walkthrough:
-------------------
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
          L                       R

Step 1: L=0, R=8, heights=[1,7], area=min(1,7)×8=8
        height[L]=1 < height[R]=7, move L
        
Step 2: L=1, R=8, heights=[8,7], area=min(8,7)×7=49 ← MAX!
        height[L]=8 > height[R]=7, move R

Step 3: L=1, R=7, heights=[8,3], area=min(8,3)×6=18
        height[L]=8 > height[R]=3, move R
        
... continue until pointers meet


How we move the pointers:
--------------------------
- If height[left] < height[right], move left pointer right
- If height[left] > height[right], move right pointer left
- If height[left] == height[right], move both pointers inward -> why? if both are equal, moving only one won't change the area.

================================================================================
IMPLEMENTATION:
================================================================================
"""

from typing import List


def max_area(height: List[int]) -> int:
    """
    Find maximum water container area using two pointers.
    Greedy approach: always move the shorter line.
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        max_water = max(max_water, current_area)
        
        # Move the pointer at shorter line (greedy choice)
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    
    return max_water


def max_area_brute_force(height: List[int]) -> int:
    """
    Brute force O(n²) for comparison/verification.
    Check all pairs of lines.
    """
    max_water = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            max_water = max(max_water, area)
    
    return max_water


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TWO POINTERS APPROACH:
----------------------
TIME COMPLEXITY: O(n)
- Each pointer moves at most n times total
- Combined movements = n - 1
- Single pass through array

SPACE COMPLEXITY: O(1)
- Only two pointers and a few variables
- No additional data structures

BRUTE FORCE COMPARISON:
-----------------------
TIME COMPLEXITY: O(n²)
- Check all n×(n-1)/2 pairs

| Approach      | Time   | Space | Notes                        |
|---------------|--------|-------|------------------------------|
| Brute Force   | O(n²)  | O(1)  | Check all pairs              |
| Two Pointers  | O(n)   | O(1)  | Greedy elimination of pairs  |

================================================================================
INTERVIEW TIPS:
================================================================================

1. CLARIFYING QUESTIONS TO ASK:
   - "Is the container formed by vertical lines only?" (yes)
   - "Can lines have height 0?" (yes)
   - "What if all lines have the same height?"
   - "What's the minimum array length?" (2)

2. EDGE CASES TO MENTION:
   - Two elements → only one possible container
   - All same height → first and last lines optimal
   - Descending heights → shrinking options
   - One very tall line → might not be in optimal solution

3. KEY EXPLANATION POINTS:
   - "Area is limited by the SHORTER line"
   - "We start with maximum width"
   - "Moving shorter line is only way to potentially improve"
   - "Moving taller line can only decrease area (width shrinks, height still limited)"

4. PROVING THE GREEDY CHOICE:
   "If the left line is shorter, any container using left as one boundary
    and ANY line between left+1 and right as the other boundary will have
    smaller width AND the same or smaller height limitation. So we can
    safely eliminate all those possibilities by moving left."

5. COMMON MISTAKES:
   - Moving both pointers at once
   - Moving the taller pointer (misses optimal)
   - Using left <= right instead of left < right
   - Forgetting to update max before moving pointer

6. RELATED PROBLEMS:
   - Trapping Rain Water (harder - considers multiple containers)
   - Largest Rectangle in Histogram (stack-based)

================================================================================
VISUAL COMPARISON: Why Move Shorter?
================================================================================

height = [3, 1, 8]
          L     R

If we move L (the shorter one):
  - We MIGHT find taller line, potentially larger area
  
If we move R (the taller one):
  - New area ≤ height[L] × (smaller width)
  - Always WORSE than current, guaranteed loss

This greedy choice eliminates configurations that CANNOT be optimal.

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        # (height, expected)
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),   # Classic example
        ([1, 1], 1),                           # Minimum case
        ([4, 3, 2, 1, 4], 16),                 # Same height at ends
        ([1, 2, 1], 2),                        # Small array
        ([1, 2, 4, 3], 4),                     # Rising then falling
        ([2, 3, 4, 5, 18, 17, 6], 17),        # Tall lines in middle
        ([1, 3, 2, 5, 25, 24, 5], 24),        # Very tall adjacent lines
        ([1, 8, 100, 2, 100, 4, 8, 3, 7], 200), # Tall lines not at ends
        ([5, 5, 5, 5, 5], 20),                 # All same height
        ([10, 1, 1, 1, 1, 1, 10], 60),        # Tall ends, short middle
    ]
    
    print("=" * 60)
    print("CONTAINER WITH MOST WATER - TEST RESULTS")
    print("=" * 60)
    
    all_passed = True
    for i, (height, expected) in enumerate(test_cases, 1):
        result = max_area(height)
        brute = max_area_brute_force(height)  # Verify with brute force
        passed = result == expected and result == brute
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:    height={height}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        if result != brute:
            print(f"  Brute:    {brute} (MISMATCH!)")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {'All tests passed!' if all_passed else 'Some tests failed.'}")
    print("=" * 60)
    
    # Verbose example
    print("\n" + "=" * 60)
    print("VERBOSE WALKTHROUGH:")
    print("=" * 60)
    max_area_verbose([1, 8, 6, 2, 5, 4, 8, 3, 7])


if __name__ == "__main__":
    run_tests()

