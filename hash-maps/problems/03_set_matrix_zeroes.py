"""
================================================================================
PROBLEM: Set Matrix Zeroes
================================================================================

QUESTION:
---------
Given an m x n integer matrix `matrix`, if an element is 0, set its entire row 
and column to 0's. You must do it in place.

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]
    Explanation: The element at (1,1) is 0, so row 1 and column 1 are set to 0.

Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    Explanation: The elements at (0,0) and (0,3) are 0, so:
                 - Row 0 is set to 0
                 - Column 0 is set to 0
                 - Column 3 is set to 0

Constraints:
    - m == matrix.length
    - n == matrix[0].length
    - 1 <= m, n <= 200
    - -2^31 <= matrix[i][j] <= 2^31 - 1

Follow-up:
    - A straightforward solution using O(mn) space is probably a bad idea.
    - A simple improvement uses O(m + n) space, but still not the best solution.
    - Could you devise a constant space solution?

================================================================================
INTUITION:
================================================================================

Why Hash Sets Work Here:
------------------------
1. TRACK ROWS AND COLUMNS TO ZERO
   - Need to remember which rows and columns contain zeros
   - Hash sets provide O(1) lookup and avoid duplicates
   - Without sets: O(mn) space to mark each cell, or O(mn) time to scan repeatedly

2. TWO-PASS APPROACH
   - First pass: Identify all rows and columns with zeros
   - Second pass: Set those rows and columns to zero
   - This prevents overwriting zeros we need to detect

3. WHY NOT MODIFY IN PLACE IMMEDIATELY?
   - If we set zeros immediately, we lose information about original zeros
   - Example: matrix[0][0] = 0, we set row 0 to zeros
   - Now matrix[0][1] = 0, but we can't tell if it was originally 0
   - Solution: Mark rows/columns first, then apply changes

Visual Walkthrough:
-------------------
Example 1:
Initial matrix:
  [1, 1, 1]
  [1, 0, 1]  ← Zero at (1,1)
  [1, 1, 1]

Step 1: Identify zeros
  - Found zero at (1,1)
  - rows_to_zero = {1}
  - cols_to_zero = {1}

Step 2: Apply zeros
  Row 1: [1, 0, 1] → [0, 0, 0]
  Col 1: [1, 0, 1] → [0, 0, 0]
  
Result:
  [1, 0, 1]
  [0, 0, 0]
  [1, 0, 1]

Example 2:
Initial matrix:
  [0, 1, 2, 0]  ← Zeros at (0,0) and (0,3)
  [3, 4, 5, 2]
  [1, 3, 1, 5]

Step 1: Identify zeros
  - Found zeros at (0,0) and (0,3)
  - rows_to_zero = {0}
  - cols_to_zero = {0, 3}

Step 2: Apply zeros
  Row 0: [0, 1, 2, 0] → [0, 0, 0, 0]
  Col 0: [0, 3, 1] → [0, 0, 0]
  Col 3: [0, 2, 5] → [0, 0, 0]
  
Result:
  [0, 0, 0, 0]
  [0, 4, 5, 0]
  [0, 3, 1, 0]

================================================================================
IMPLEMENTATION:
================================================================================
"""

from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Set entire rows and columns to zero where zeros are found.
    Uses hash sets to track which rows and columns need to be zeroed.
    Time: O(m*n), Space: O(m+n)
    """
    m, n = len(matrix), len(matrix[0])
    
    # Use sets to track rows and columns that need to be zeroed
    rows_to_zero = set()
    cols_to_zero = set()
    
    # First pass: Identify all rows and columns with zeros
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)
    
    # Second pass: Set identified rows and columns to zero
    for i in range(m):
        for j in range(n):
            if i in rows_to_zero or j in cols_to_zero:
                matrix[i][j] = 0


def setZeroes_optimized(matrix: List[List[int]]) -> None:
    """
    Optimized version using first row and column as markers.
    Constant space O(1) solution (excluding input matrix).
    Time: O(m*n), Space: O(1)
    """
    m, n = len(matrix), len(matrix[0])
    
    # Check if first row and column have zeros
    first_row_has_zero = False
    first_col_has_zero = False

    for i in range(m):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_has_zero = True
            break
    
    # Use first row and column as markers
    # If matrix[i][j] == 0, mark matrix[i][0] = 0 and matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark row
                matrix[0][j] = 0  # Mark column
    
    # Set zeros based on markers (skip first row/col for now)
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Handle first row
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0
    
    # Handle first column
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0


def setZeroes_boolean_flags(matrix: List[List[int]]) -> None:
    """
    Alternative using boolean lists instead of sets.
    Functionally similar to setZeroes(), just different data structure.
    Time: O(m*n), Space: O(m+n)
    """
    m, n = len(matrix), len(matrix[0])
    
    # Boolean arrays to track rows and columns
    rows_to_zero = [False] * m
    cols_to_zero = [False] * n
    
    # First pass: Mark rows and columns
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_to_zero[i] = True
                cols_to_zero[j] = True
    
    # Second pass: Apply zeros
    for i in range(m):
        for j in range(n):
            if rows_to_zero[i] or cols_to_zero[j]:
                matrix[i][j] = 0


def setZeroes_naive(matrix: List[List[int]]) -> None:
    """
    Naive approach: Mark cells to zero, then apply.
    Uses O(mn) space to store which cells to zero.
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(matrix), len(matrix[0])
    cells_to_zero = []
    
    # Find all zeros
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                cells_to_zero.append((i, j))
    
    # Set entire rows and columns to zero
    for i, j in cells_to_zero:
        # Set row to zero
        for col in range(n):
            matrix[i][col] = 0
        # Set column to zero
        for row in range(m):
            matrix[row][j] = 0


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TIME COMPLEXITY: O(m * n)
- First pass: O(m * n) to identify zeros
- Second pass: O(m * n) to set zeros
- Total: O(m * n)

SPACE COMPLEXITY: O(m + n)
- Sets store at most m rows and n columns
- In worst case: all rows or all columns have zeros
- Total: O(m + n)

COMPARISON WITH ALTERNATIVES:
-----------------------------
| Approach          | Time    | Space   | Notes                          |
|-------------------|---------|---------|--------------------------------|
| Naive (O(mn))     | O(m*n)  | O(m*n)  | Store all zero positions       |
| Hash Sets         | O(m*n)  | O(m+n)  | Best readable solution          |
| Boolean Arrays    | O(m*n)  | O(m+n)  | Similar to sets, fixed size    |
| In-place markers  | O(m*n)  | O(1)    | Use first row/col as markers   |

Note: The O(1) space solution is more complex and harder to understand.
The O(m+n) space solution with sets is usually preferred in interviews.

================================================================================
INTERVIEW TIPS:
================================================================================

1. CLARIFYING QUESTIONS TO ASK:
   - "Should I modify the matrix in place?" (Yes, usually)
   - "What if there are multiple zeros in the same row/column?" (Set once)
   - "Can the matrix contain negative numbers?" (Yes, only 0 triggers change)
   - "What's the range of matrix dimensions?" (Usually 1-200)
   - "Should I return the matrix or modify it?" (Usually modify in place)

2. EDGE CASES TO MENTION:
   - Single cell matrix (1x1)
   - All zeros matrix
   - No zeros matrix (no changes)
   - Single row or single column
   - Zeros only in first row/column (for optimized solution)
   - Multiple zeros in same row/column

3. OPTIMIZATION TALKING POINTS:
   - "I'll use hash sets to track rows and columns efficiently"
   - "Two-pass approach: identify first, then modify"
   - "This prevents losing information about original zeros"
   - "O(m+n) space is better than O(mn) naive approach"
   - "Can optimize to O(1) space using first row/col as markers"

4. COMMON MISTAKES:
   - Modifying matrix while iterating (loses original zero positions)
   - Not handling first row/column separately in optimized solution
   - Forgetting to check if first row/col originally had zeros
   - Setting zeros before identifying all positions
   - Off-by-one errors in row/column indices

5. FOLLOW-UP QUESTIONS:
   - "Can you do it in O(1) space?" → Use first row/col as markers
   - "What if we can't modify first row/col?" → Use separate variables
   - "What if matrix is very sparse?" → Only track non-zero positions
   - "What if we want to return new matrix?" → Create copy first
   - "What if we need to preserve original?" → Work on copy

6. WHY HASH SETS OVER OTHER APPROACHES:
   - vs Lists: Sets provide O(1) membership testing
   - vs Boolean arrays: Sets avoid duplicates automatically
   - vs Naive O(mn): Much less space, same time complexity
   - vs In-place markers: More readable, easier to understand

7. TWO-PASS STRATEGY EXPLANATION:
   - Why not one pass? If we set zeros immediately, we lose track of
     which zeros were original vs which we just set
   - First pass: Build sets of rows/columns to zero
   - Second pass: Apply zeros based on sets
   - This ensures we don't miss any zeros

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        # Test case 1: Single zero (Example 1)
        ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
        
        # Test case 2: Multiple zeros in first row (Example 2)
        ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
        
        # Test case 3: No zeros
        ([[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6],[7,8,9]]),
        
        # Test case 4: All zeros
        ([[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]),
        
        # Test case 5: Single cell
        ([[0]], [[0]]),
        
        # Test case 6: Single row
        ([[1,0,2,3]], [[0,0,0,0]]),
        
        # Test case 7: Single column
        ([[1],[0],[2],[3]], [[0],[0],[0],[0]]),
        
        # Test case 8: Zeros in same row
        ([[1,0,2,0],[3,4,5,6],[7,8,9,10]], [[0,0,0,0],[3,0,5,0],[7,0,9,0]]),
        
        # Test case 9: Zeros in same column
        ([[1,2,3],[0,4,5],[0,6,7]], [[0,2,3],[0,0,0],[0,0,0]]),
        
        # Test case 10: Zero at (0,0)
        ([[0,1,2],[3,4,5],[6,7,8]], [[0,0,0],[0,4,5],[0,7,8]]),
    ]
    
    print("=" * 60)
    print("SET MATRIX ZEROES - TEST RESULTS")
    print("=" * 60)
    
    all_passed = True
    for i, (input_matrix, expected) in enumerate(test_cases, 1):
        # Create a copy since we modify in place
        matrix = [row[:] for row in input_matrix]
        setZeroes(matrix)
        passed = matrix == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:    {input_matrix}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {matrix}")
        if not passed:
            print("  ❌ MISMATCH!")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {'All tests passed!' if all_passed else 'Some tests failed.'}")
    print("=" * 60)
    
    # Test optimized version
    print("\n" + "=" * 60)
    print("TESTING OPTIMIZED VERSION (O(1) space)")
    print("=" * 60)
    
    all_passed_opt = True
    for i, (input_matrix, expected) in enumerate(test_cases, 1):
        matrix = [row[:] for row in input_matrix]
        setZeroes_optimized(matrix)
        passed = matrix == expected
        all_passed_opt = all_passed_opt and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        if not passed:
            print(f"\nTest {i}: {status}")
            print(f"  Input:    {input_matrix}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {matrix}")
    
    if all_passed_opt:
        print("\n✓ All optimized tests passed!")
    else:
        print(f"\n✗ {sum(1 for _ in test_cases if True)} optimized tests failed")


if __name__ == "__main__":
    run_tests()

