"""
================================================================================
PROBLEM: Valid Palindrome
================================================================================

QUESTION:
---------
A phrase is a palindrome if, after converting all uppercase letters to lowercase
and removing all non-alphanumeric characters, it reads the same forward and 
backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: After removing non-alphanumeric characters, s is empty "".
                 An empty string is a palindrome by definition.

Constraints:
    - 1 <= s.length <= 2 * 10^5
    - s consists only of printable ASCII characters.

================================================================================
INTUITION:
================================================================================

Why Two Pointers? SYMMETRY = INWARD TRAVERSAL
---------------------------------------------
A palindrome is symmetric around its center. This symmetry is a "predictable 
dynamic" - we can compare characters from both ends moving inward.

Key Insight:
- If s[left] == s[right] for all pairs → palindrome
- If any pair differs → not a palindrome
- We can stop early on first mismatch!

Visual Walkthrough:
-------------------
s = "A man, a plan, a canal: Panama"

After cleanup: "amanaplanacanalpanama"

Step 1: "amanaplanacanalpanama"
         L                   R   → 'a' == 'a' ✓

Step 2: "amanaplanacanalpanama"
          L                 R    → 'm' == 'm' ✓

Step 3: "amanaplanacanalpanama"
           L               R     → 'a' == 'a' ✓
         
... (continue until pointers meet)

All pairs match → PALINDROME!

Two Approaches:
--------------
1. Clean string first, then compare → O(n) space for cleaned string
2. Compare in-place, skip non-alphanumeric → O(1) space (preferred!)

================================================================================
IMPLEMENTATION:
================================================================================
"""


def is_palindrome(s: str) -> bool:
    """
    Check if string is palindrome using two pointers (O(1) space).
    Skips non-alphanumeric characters in-place.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def is_palindrome_clean_first(s: str) -> bool:
    """
    Alternative: Clean string first, then compare.
    More readable but uses O(n) space.
    """
    # Clean: keep only alphanumeric, convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Compare with reverse
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointer_on_cleaned(s: str) -> bool:
    """
    Alternative: Clean string, then use two pointers.
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


"""
================================================================================
COMPLEXITY ANALYSIS:
================================================================================

APPROACH 1: In-place Two Pointers (Preferred)
---------------------------------------------
TIME COMPLEXITY: O(n)
- Each character visited at most once
- left only moves right, right only moves left

SPACE COMPLEXITY: O(1)
- Only two pointer variables
- No additional string created

APPROACH 2: Clean First
-----------------------
TIME COMPLEXITY: O(n)
- O(n) to clean string
- O(n) to reverse and compare

SPACE COMPLEXITY: O(n)
- Cleaned string takes O(n) space

COMPARISON:
-----------
| Approach           | Time  | Space | Notes                    |
|--------------------|-------|-------|--------------------------|
| In-place pointers  | O(n)  | O(1)  | Best! Single pass        |
| Clean + reverse    | O(n)  | O(n)  | More readable, but space |
| Clean + pointers   | O(n)  | O(n)  | Combines worst of both   |

================================================================================
INTERVIEW TIPS:
================================================================================

1. CLARIFYING QUESTIONS TO ASK:
   - "Should I consider only alphanumeric characters?"
   - "Is the comparison case-insensitive?"
   - "How should I handle empty strings or strings with only spaces?"
   - "What counts as alphanumeric? Letters and numbers only?"

2. EDGE CASES TO MENTION:
   - Empty string → true (vacuously a palindrome)
   - Single character → true
   - String with only non-alphanumeric → true (empty after cleaning)
   - All same characters → true
   - Numbers in string: "12321" → true

3. KEY DISCUSSION POINTS:
   - "Palindrome has symmetry - perfect for inward traversal"
   - "I can do this in O(1) space by skipping characters in-place"
   - "versus O(n) space if I create a cleaned copy first"

4. COMMON MISTAKES:
   - Forgetting case-insensitive comparison
   - Not handling empty string (should return true)
   - Not handling non-alphanumeric characters
   - Using `left <= right` instead of `left < right` (causes issues)

5. VARIATIONS TO KNOW:
   - Valid Palindrome II: Can remove at most one character
   - Longest Palindromic Substring (different technique)
   - Palindrome Linked List

6. FOLLOW-UP: Valid Palindrome II
   - "What if we can remove at most one character?"
   - Answer: On mismatch, try skipping left OR right, check both

================================================================================
BONUS: Valid Palindrome II (Follow-up)
================================================================================
"""


def valid_palindrome_ii(s: str) -> bool:
    """
    Can form palindrome by removing at most one character.
    """
    def is_palindrome_range(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            # Try skipping either left or right character
            return (is_palindrome_range(left + 1, right) or 
                    is_palindrome_range(left, right - 1))
        left += 1
        right -= 1
    
    return True


"""
================================================================================
TEST CASES:
================================================================================
"""


def run_tests():
    test_cases = [
        # (s, expected)
        ("A man, a plan, a canal: Panama", True),  # Classic palindrome
        ("race a car", False),                      # Not a palindrome
        (" ", True),                                # Empty after cleaning
        ("", True),                                 # Empty string
        ("a", True),                                # Single character
        ("aa", True),                               # Two same characters
        ("ab", False),                              # Two different characters
        ("Aa", True),                               # Case insensitive
        ("0P", False),                              # Alphanumeric mix
        ("12321", True),                            # Numeric palindrome
        (".,", True),                               # Only punctuation
        ("Was it a car or a cat I saw?", True),    # Another classic
        ("No 'x' in Nixon", True),                  # With quotes
        ("hello", False),                           # Simple non-palindrome
    ]
    
    print("=" * 60)
    print("VALID PALINDROME - TEST RESULTS")
    print("=" * 60)
    
    all_passed = True
    for i, (s, expected) in enumerate(test_cases, 1):
        result = is_palindrome(s)
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:    \"{s}\"")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
    
    print("\n" + "=" * 60)
    print("VALID PALINDROME II - TEST RESULTS")
    print("=" * 60)
    
    test_cases_ii = [
        ("aba", True),         # Already palindrome
        ("abca", True),        # Remove 'c' or 'b'
        ("abc", False),        # Can't make palindrome with one removal
        ("deeee", True),       # Remove first 'd'
        ("", True),            # Empty string
        ("a", True),           # Single character
    ]
    
    for i, (s, expected) in enumerate(test_cases_ii, 1):
        result = valid_palindrome_ii(s)
        passed = result == expected
        all_passed = all_passed and passed
        
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:    \"{s}\"")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: {'All tests passed!' if all_passed else 'Some tests failed.'}")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()

