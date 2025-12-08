"""
================================================================================
PROBLEM: Valid Sudoku
================================================================================

QUESTION:
---------
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
   without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily 
  solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:
    Input: board = 
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

Example 2:
    Input: board = 
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner 
    being changed to 8. Since there are two 8's in the top left 3x3 sub-box, 
    it is invalid.

Constraints:
    - board.length == 9
    - board[i].length == 9
    - board[i][j] is a digit 1-9 or '.'.

================================================================================
INTUITION:
================================================================================

Why Hash Maps/Sets Work Here:
------------------------------
1. TRACK SEEN VALUES EFFICIENTLY
   - Need to check if a digit appears more than once in row/column/box
   - Hash set provides O(1) lookup and insertion
   - Without hash set: O(n) lookup per check = O(n²) total

2. THREE SEPARATE TRACKING SYSTEMS
   - Rows: 9 sets (one per row)
   - Columns: 9 sets (one per column)
   - Boxes: 9 sets (one per 3x3 box)
   - Each cell belongs to exactly one row, one column, and one box

3. EFFICIENT BOX INDEXING
   - Box index = (row // 3) * 3 + (col // 3)
   - This maps 9x9 grid to 9 boxes (0-8)
   - Example: (4, 5) → (4//3)*3 + (5//3) = 1*3 + 1 = 4 (box 4)

Visual Walkthrough:
-------------------
Example 1 (Valid):
Row 0: ["5","3",".",".","7",".",".",".","."]
- row_sets[0] = {"5", "3", "7"} ✓

Column 0: ["5","6",".","8","4","7",".",".","."]
- col_sets[0] = {"5", "6", "8", "4", "7"} ✓

Box 0 (top-left 3x3):
  ["5","3","."]
  ["6",".","."]
  [".","9","8"]
- box_sets[0] = {"5", "3", "6", "9", "8"} ✓

Example 2 (Invalid):
Row 0: ["8","3",".",".","7",".",".",".","."]
- row_sets[0] = {"8", "3", "7"} ✓

Box 0 (top-left 3x3):
  ["8","3","."]
  ["6",".","."]
  [".","9","8"]  ← Two 8's in same box!
- box_sets[0] = {"8", "3", "6", "9"} → Try to add "8" again → ✗ INVALID!

================================================================================
IMPLEMENTATION:
================================================================================
"""

from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    """
    Validate Sudoku board using hash sets for rows, columns, and boxes.
    Time: O(1) - fixed 9x9 grid, Space: O(1) - fixed number of sets
    """
    # Initialize sets for rows, columns, and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            
            # Skip empty cells
            if cell == '.':
                continue
            
            # Calculate box index: (i // 3) * 3 + (j // 3)
            box_idx = (i // 3) * 3 + (j // 3)
            
            # Check if digit already exists in row, column, or box
            if cell in rows[i] or cell in cols[j] or cell in boxes[box_idx]:
                return False
            
            # Add to all three sets
            rows[i].add(cell)
            cols[j].add(cell)
            boxes[box_idx].add(cell)
    
    return True


def isValidSudoku_alternative(board: List[List[str]]) -> bool:
    """
    Alternative implementation using string keys for tracking.
    Uses format: "digit in row/col/box" as keys in a single set.
    More memory efficient (one set instead of 27 sets).
    """
    seen = set()
    
    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            
            if cell == '.':
                continue
            
            box_idx = (i // 3) * 3 + (j // 3)
            
            # Create unique keys for row, column, and box
            row_key = f"{cell} in row {i}"
            col_key = f"{cell} in col {j}"
            box_key = f"{cell} in box {box_idx}"
            
            # If any key already exists, we have a duplicate
            if row_key in seen or col_key in seen or box_key in seen:
                return False
            
            seen.add(row_key)
            seen.add(col_key)
            seen.add(box_key)
    
    return True


def isValidSudoku_compact(board: List[List[str]]) -> bool:
    """
    Most compact version using tuple keys.
    Uses (row, digit), (col, digit), (box, digit) tuples.
    """
    seen = set()
    
    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell != '.':
                box_idx = (i // 3) * 3 + (j // 3)
                # Try to add all three keys - if any fails, return False
                if not (seen.add((i, cell)) and 
                        seen.add((9 + j, cell)) and 
                        seen.add((18 + box_idx, cell))):
                    return False
    
    return True


def isValidSudoku_brute_force(board: List[List[str]]) -> bool:
    """
    Brute force approach for comparison.
    Checks each row, column, and box separately.
    Time: O(1) but more operations, Space: O(1)
    """
    # Check rows
    for row in board:
        seen = set()
        for cell in row:
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)
    
    # Check columns
    for j in range(9):
        seen = set()
        for i in range(9):
            cell = board[i][j]
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)
    
    # Check boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            seen = set()
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    cell = board[i][j]
                    if cell != '.':
                        if cell in seen:
                            return False
                        seen.add(cell)
    
    return True


def isValidSudoku_class_style(board: List[List[str]]) -> bool:
    """
    Class-style implementation using 2D list for subgrids.
    Uses separate if-else blocks for each check.
    Note: Fixed bug - changed column[i] to column[j]
    """
    row = [set() for _ in range(9)]
    column = [set() for _ in range(9)]
    subgrid = [[set() for _ in range(3)] for _ in range(3)]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            val = board[i][j]
            if val == '.':
                continue
            
            if val in row[i]:
                return False
            else:
                row[i].add(val)
            
            # Fixed: was column[i], should be column[j]
            if val in column[j]:
                return False
            else:
                column[j].add(val)
            
            if val in subgrid[i//3][j//3]:
                return False
            else:
                subgrid[i//3][j//3].add(val)
    
    return True


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

TIME COMPLEXITY: O(1)
- Fixed 9x9 grid = 81 cells to check
- Each cell: O(1) hash set operations (add, lookup)
- Total: O(81) = O(1) constant time

SPACE COMPLEXITY: O(1)
- Fixed number of hash sets: 9 rows + 9 columns + 9 boxes = 27 sets
- Each set can hold at most 9 digits
- Total: O(27 * 9) = O(243) = O(1) constant space

COMPARISON WITH ALTERNATIVES:
-----------------------------
| Approach          | Time    | Space   | Notes                          |
|-------------------|---------|---------|--------------------------------|
| Brute Force       | O(1)    | O(1)    | Three separate passes          |
| Hash Sets (3x9)   | O(1)    | O(1)    | One pass, clear structure      |
| Single Set (keys) | O(1)    | O(1)    | One pass, one set, less memory |
| Array of bools    | O(1)    | O(1)    | Similar to sets, fixed size    |

Note: All approaches are O(1) because grid size is fixed. The difference is
in code clarity and constant factors.

================================================================================
INTERVIEW TIPS:
================================================================================

1. CLARIFYING QUESTIONS TO ASK:
   - "Is the board always 9x9?" (Yes, standard Sudoku)
   - "What characters represent empty cells?" (Usually '.' or '0')
   - "Are digits stored as strings or integers?" (Usually strings)
   - "Do I need to solve it or just validate?" (Just validate)
   - "What should I return if board is empty?" (True, empty is valid)

2. EDGE CASES TO MENTION:
   - Empty board (all '.' cells) → Valid
   - Completely filled valid board → Valid
   - Duplicate in row → Invalid
   - Duplicate in column → Invalid
   - Duplicate in box → Invalid
   - Multiple duplicates → Return False on first duplicate found

3. OPTIMIZATION TALKING POINTS:
   - "I'll use hash sets for O(1) duplicate detection"
   - "One-pass solution: check all three constraints simultaneously"
   - "Box indexing formula: (row//3)*3 + (col//3)"
   - "Early termination: return False as soon as duplicate found"

4. COMMON MISTAKES:
   - Forgetting to skip '.' (empty cells)
   - Incorrect box index calculation
   - Checking rows/columns/boxes separately (less efficient)
   - Using lists instead of sets (O(n) lookup vs O(1))
   - Off-by-one errors in box boundaries

5. FOLLOW-UP QUESTIONS:
   - "How would you solve the Sudoku?" → Backtracking algorithm
   - "What if board is NxN?" → Generalize box size to sqrt(N)
   - "What if we want to find all invalid cells?" → Return list of positions
   - "What if digits can be 0-9?" → Same approach, adjust validation
   - "How to optimize for sparse boards?" → Only track filled cells

6. WHY HASH SETS OVER OTHER APPROACHES:
   - vs Arrays: Sets provide O(1) membership testing
   - vs Lists: Sets prevent duplicates automatically
   - vs Sorting: No need to sort, just check existence
   - vs Bitmasking: More readable, works for any digit range

7. BOX INDEX CALCULATION EXPLANATION:
   - Row 0-2, Col 0-2 → Box 0
   - Row 0-2, Col 3-5 → Box 1
   - Row 0-2, Col 6-8 → Box 2
   - Row 3-5, Col 0-2 → Box 3
   - etc.
   - Formula: box = (row // 3) * 3 + (col // 3)
   - This groups cells into 3x3 boxes numbered 0-8

================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        # Test case 1: Valid board (Example 1)
        ([["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]], True),
        
        # Test case 2: Invalid - duplicate in box (Example 2)
        ([["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]], False),
        
        # Test case 3: Empty board (all dots)
        ([["."]*9 for _ in range(9)], True),
        
        # Test case 4: Invalid - duplicate in row
        ([["5","5",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]], False),
        
        # Test case 5: Invalid - duplicate in column
        ([["5","3",".",".","7",".",".",".","."]
         ,["5",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]], False),
        
        # Test case 6: Valid - completely filled valid board
        ([["5","3","4","6","7","8","9","1","2"]
         ,["6","7","2","1","9","5","3","4","8"]
         ,["1","9","8","3","4","2","5","6","7"]
         ,["8","5","9","7","6","1","4","2","3"]
         ,["4","2","6","8","5","3","7","9","1"]
         ,["7","1","3","9","2","4","8","5","6"]
         ,["9","6","1","5","3","7","2","8","4"]
         ,["2","8","7","4","1","9","6","3","5"]
         ,["3","4","5","2","8","6","1","7","9"]], True),
        
        # Test case 7: Invalid - duplicate in different box
        ([["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,["5",".",".",".","8",".",".","7","9"]], False),  # Duplicate 5 in col 0
    ]
    
    print("=" * 60)
    print("VALID SUDOKU - TEST RESULTS")
    print("=" * 60)
    
    all_passed = True
    for i, (board, expected) in enumerate(test_cases, 1):
        result = isValidSudoku(board)
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        if not passed:
            print(f"  Board preview (first row): {board[0]}")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {'All tests passed!' if all_passed else 'Some tests failed.'}")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()

