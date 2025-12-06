# Two Pointer Technique

## Core Concept
A single pointer tracks one element at a time. By introducing a second pointer, we can compare elements at two different positions simultaneously, enabling efficient decisions based on relationships between values.

**Key Insight:** Sorted arrays provide predictable dynamics—when we move a pointer in a sorted array, we can predict whether the next value will be greater or smaller. This predictability is what makes two pointers powerful.

---

## Three Main Strategies

### 1. Inward Traversal (Opposite Direction)
Pointers start at opposite ends of the data structure and traverse toward the center. Positions are adjusted based on comparisons until a condition is met or they meet/cross each other.

**Best for:** Problems comparing elements from both ends
- Pair sum in sorted array
- Container with most water
- Valid palindrome
- Trapping rain water

```
[1, 2, 3, 4, 5, 6, 7]
 L →             ← R
```

### 2. Unidirectional Traversal (Same Direction)
Both pointers move in the same direction. One pointer (usually right/fast) searches for information, while the other (left/slow) keeps track of a position or condition.

**Best for:** In-place array modifications, partitioning
- Remove duplicates from sorted array
- Move zeros to end
- Remove element in-place
- Partition array

```
[0, 1, 0, 3, 12]
 L
 R →
```

### 3. Staged Traversal
The first pointer searches for something specific. Once found, a second pointer gathers additional information related to the first pointer's position.

**Best for:** Finding subsequences or dependent pairs
- Three sum (fix one, use two pointers for remaining)
- Subarray problems

```
Stage 1: Fix first pointer (i)
[-4, -1, -1, 0, 1, 2]
  i

Stage 2: Use two pointers on remaining subarray
[-4, -1, -1, 0, 1, 2]
  i   L →        ← R

Stage 3: Move to next fixed position
[-4, -1, -1, 0, 1, 2]
      i   L →   ← R
```

---

## When to Use Two Pointers

### Required Conditions
1. **Linear data structure** — arrays, strings, or linked lists
2. **Predictable dynamics** — some pattern that guides pointer movement

### Indicators the Pattern May Apply
- Input is **sorted** or can be sorted
- Looking for a **pair** or **triplet** of values meeting a condition
- Need to compare elements at **different positions**
- Problem involves **symmetry** (palindromes)
- Requires **in-place** modifications with O(1) space
- Finding **subarrays** or **substrings** with specific properties

---

## Complexity Analysis

| Aspect | Typical Complexity |
|--------|-------------------|
| Time   | O(n) or O(n²) with nested loops |
| Space  | O(1) — main advantage over hash-based approaches |

**Trade-off:** Two pointers often sacrifice the O(1) lookup of hash tables for O(1) space complexity.

---

## Related Techniques

### Fast and Slow Pointers (Floyd's Algorithm)
A variation where pointers move at different speeds. Commonly used for:
- Detecting cycles in linked lists
- Finding middle of linked list
- Finding the start of a cycle

### Sliding Window
A specialized form of two pointers where:
- Both pointers move in the same direction
- The "window" between them represents a contiguous subarray/substring
- Window expands (right pointer) and contracts (left pointer) based on conditions

**Use sliding window when:** Looking for contiguous subarrays/substrings with specific properties (max sum, unique characters, etc.)

---

## Common Patterns & Templates

### Pattern 1: Inward (Two Sum in Sorted Array)
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### Pattern 2: Unidirectional (Remove Duplicates)
```python
def remove_duplicates(arr):
    if not arr:
        return 0
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1
    return write 
```

### Pattern 3: Three Sum (Staged + Inward)
```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, len(nums) - 1
        # inward
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # remove duplicates 

                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
```

---

## Common Mistakes to Avoid
1. **Off-by-one errors** — be careful with `left < right` vs `left <= right`
2. **Forgetting to move pointers** — can cause infinite loops
3. **Not handling duplicates** — especially in problems asking for unique results
4. **Assuming sorted input** — verify or sort first if needed

---

## Practice Problems (by difficulty)

### Easy
- Two Sum II (sorted array)
- Valid Palindrome
- Merge Sorted Array
- Move Zeroes

### Medium
- Three Sum
- Container With Most Water
- Remove Duplicates from Sorted Array II
- Sort Colors (Dutch National Flag)

### Hard
- Trapping Rain Water
- Minimum Window Substring (sliding window)
