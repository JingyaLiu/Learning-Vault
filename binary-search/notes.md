# Binary Search

## Core Concept
Binary search is an efficient algorithm for finding a value in a sorted dataset. It works by repeatedly dividing the search space in half, eliminating half of the remaining elements at each step.

**Key Insight:** By comparing the target value with the middle element, we can determine which half of the array contains the target, allowing us to discard the other half. This divide-and-conquer approach achieves O(log n) time complexity, making it much faster than linear search for large datasets.

---

## How It Works

### Basic Steps
1. **Define the search window** — initialize `left` and `right` pointers to define the current search space
2. **Calculate the middle point** — `mid = (left + right) // 2` or `mid = left + (right - left) // 2` (to avoid overflow)
3. **Compare and narrow down** — compare the target with `arr[mid]`:
   - If `target == arr[mid]`: found the target
   - If `target < arr[mid]`: search in the left half (`right = mid - 1`)
   - If `target > arr[mid]`: search in the right half (`left = mid + 1`)
4. **Repeat** until the target is found or the search space is exhausted

### Visualization
```
Searching for 7 in [1, 3, 5, 7, 9, 11, 13]:
[1, 3, 5, 7, 9, 11, 13]
 L        M           R  (M=7, found!)

Searching for 6 in [1, 3, 5, 7, 9, 11, 13]:
[1, 3, 5, 7, 9, 11, 13]
 L        M          R  (M=7, 6<7, go left)
[1, 3, 5]
 L  M  R            (M=3, 6>3, go right)
       [5]
       LMR             (M=5, 6>5, go right)
       []              (empty, not found)
```

---

## When to Use Binary Search

### Required Conditions
1. **Sorted data** — the array must be sorted (or can be sorted)
2. **Monotonic property** — there's a pattern that allows us to eliminate half the search space
3. **Searchable property** — we can determine which half contains the answer based on a comparison

### Problem Indicators
- Keywords: "sorted array", "find target", "search in sorted"
- Looking for a specific value or position
- Finding boundaries (first/last occurrence, insertion point)
- Search space reduction problems
- Problems that can be transformed into a search problem

### When NOT to Use
- Unsorted data (unless you can sort it first)
- Need to find all occurrences (though binary search can help find boundaries)
- Data changes frequently (binary search tree might be better)

---

## Complexity Analysis

| Aspect | Complexity |
|--------|-----------|
| Time   | O(log n) — eliminates half the search space each iteration |
| Space  | O(1) — iterative version uses constant space |
|        | O(log n) — recursive version uses call stack space |

**Why O(log n)?** Each iteration eliminates half the elements. For an array of size n:
- After 1 iteration: n/2 elements remain
- After 2 iterations: n/4 elements remain
- After k iterations: n/2^k elements remain
- We stop when n/2^k = 1, so k = log₂(n)

---

## Common Patterns & Templates

### Pattern 1: Standard Binary Search (Find Exact Match)
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # not found
```

**Key points:**
- Loop condition: `left <= right` (allows checking when left == right)
- Update: `left = mid + 1` and `right = mid - 1` (exclude mid since we checked it)

### Pattern 2: Find First Occurrence (Left Boundary)
```python
def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Pattern 3: Find Last Occurrence (Right Boundary)
```python
def find_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### Pattern 4: Find Insertion Position
```python
def search_insert_position(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # insertion point
```

### Pattern 5: Binary Search on Answer (Search Space Reduction)
When the answer itself is in a searchable range, we can binary search on the answer space.

```python
def find_minimum_in_rotated_array(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]
```

**Key points:**
- Loop condition: `left < right` (stop when left == right)
- Update: `right = mid` (don't exclude mid, it might be the answer)

### Pattern 6: Search in Rotated Sorted Array
```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

---

## Decision Framework: `left <= right` vs `left < right`

### Use `left <= right` when:
- You want to check every element including when `left == right`
- You're searching for an exact match
- You update with `left = mid + 1` and `right = mid - 1`
- **Return value:** Usually `-1` if not found, or the index if found

### Use `left < right` when:
- You're finding a boundary or insertion point
- You update with `right = mid` (not excluding mid)
- The answer is guaranteed to exist in the search space
- **Return value:** Usually `left` (or `right`, they're equal when loop ends)

---

## Common Mistakes to Avoid

1. **Integer overflow** — use `mid = left + (right - left) // 2` instead of `mid = (left + right) // 2` for very large arrays
2. **Wrong loop condition** — `left <= right` vs `left < right` depends on the problem
3. **Incorrect pointer updates** — `left = mid + 1` vs `left = mid` and `right = mid - 1` vs `right = mid`
4. **Off-by-one errors** — be careful with inclusive vs exclusive bounds
5. **Not handling empty arrays** — check `if not arr: return -1`
6. **Forgetting to update pointers** — can cause infinite loops
7. **Returning wrong value** — sometimes return `left`, sometimes return `mid`, sometimes return `-1`

---

## Related Techniques

### Two Pointers
Binary search uses two pointers (`left` and `right`) to define the search space, similar to the two-pointer technique but with a different movement strategy.

### Divide and Conquer
Binary search is a classic divide-and-conquer algorithm, dividing the problem in half at each step.

### Binary Search Trees
BST operations (search, insert, delete) use binary search logic to navigate the tree structure.

---

## Practice Problems (by difficulty)

### Easy
- Binary Search
- Search Insert Position
- First Bad Version
- Sqrt(x)
- Valid Perfect Square

### Medium
- Search in Rotated Sorted Array
- Find First and Last Position of Element in Sorted Array
- Find Peak Element
- Search a 2D Matrix
- Find Minimum in Rotated Sorted Array
- Time Based Key-Value Store
- Capacity To Ship Packages Within D Days

### Hard
- Median of Two Sorted Arrays
- Split Array Largest Sum
- Kth Smallest Element in a Sorted Matrix
- Find Minimum in Rotated Sorted Array II (with duplicates)