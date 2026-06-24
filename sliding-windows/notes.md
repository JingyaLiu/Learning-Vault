# Sliding Window

## Core Concept
The sliding window technique is a subset of the two-pointer pattern. It uses two pointers to define the bounds of a "window" over an iterable (arrays, strings). The window represents a contiguous subcomponent of the data, and both pointers move in the same direction. Problems that might otherwise use two nested loops to search all possible subarrays can often be solved in O(n) time with a single pass.

**Key Insight:** Instead of checking every possible subarray (O(n²)), maintain a window that expands and shrinks based on the problem. You only add/remove one element at a time, so each element is processed at most twice—once when it enters and once when it leaves the window.

---

## How It Works

### Expand, Shrink, Slide
- **Expand** — move the right pointer to include new elements
- **Shrink** — move the left pointer to exclude elements when the window violates a condition
- **Slide** — the window “slides” forward; only the edges change, not the whole range

### Visualization
```
Fixed-size window (size k = 3):
[1, 2, 3, 4, 5, 6, 7]
 L-----R              → window = [1,2,3]
    L-----R           → window = [2,3,4]
       L-----R        → window = [3,4,5]

Dynamic window:
[1, 2, 3, 1, 2, 3, 4]   (e.g. "longest substring with ≤ 2 distinct chars")
 L  R                    → expand
 L     R                 → expand, then shrink from left when needed
    L     R
```

---

## Two Main Types

### 1. Fixed-Length Sliding Window
The window size is fixed (e.g., length `k`). Both pointers move together by one step each time.

**Best for:**
- Maximum sum of subarray of size k
- Average of subarrays of size k
- Permutation in string (anagram of size k)
- Max/min in every k-sized window

**Idea:** Compute something for the first window [0..k-1], then slide by one: drop the leftmost element, add the next right element.

### 2. Dynamic Sliding Window
The window size changes. Typically the right pointer expands, and the left pointer shrinks when the current window no longer satisfies the condition.

**Best for:**
- Longest substring with at most k distinct characters
- Minimum window substring
- Longest substring without repeating characters
- Subarray/product less than k

**Idea:** Expand right until the window is invalid, then shrink from the left until it’s valid again; track the best window seen.

---

## When to Use Sliding Window

### Problem Indicators
- **Subarray** or **substring** — contiguous segment
- **Longest** or **shortest** — substring/subarray meeting a condition
- **At most k** / **at least k** — limits on frequency, distinct chars, sum, etc.
- **All subarrays of size k** — fixed-length windows
- **Unique** / **no repeating** — often dynamic window with a frequency map

### Required Conditions
1. **Contiguous** — the result is a contiguous subarray or substring
2. **Iterable** — array or string with clear “next” position
3. **Window property** — expanding/shrinking by one element gives a way to update your result without recomputing from scratch

---

## Complexity Analysis

| Type              | Time   | Space      |
|-------------------|--------|------------|
| Fixed window      | O(n)   | O(1) or O(k) |
| Dynamic window    | O(n)   | O(k) or O(1) |
| With frequency map| O(n)   | O(min(n, alphabet)) |

**Note:** Without sliding window, “all subarrays” is O(n²). Sliding window avoids that by reusing work from the previous window.

---

## Common Patterns & Templates

### Pattern 1: Fixed Window (e.g. max sum of size k)
```python
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Pattern 2: Dynamic Window (e.g. longest substring with at most k distinct)
```python
def longest_substring_k_distinct(s, k):
    from collections import defaultdict
    if k == 0:
        return 0

    left = 0
    freq = defaultdict(int)
    max_len = 0

    for right, char in enumerate(s):
        freq[char] += 1

        while len(freq) > k:
            left_char = s[left]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

### Pattern 3: Dynamic Window (e.g. longest substring without repeating characters)
```python
def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len
```

### Pattern 4: Fixed Window (min/max in every window of size k)
```python
from collections import deque

def max_in_sliding_window(nums, k):
    dq = deque()  # indices, values in decreasing order
    result = []

    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

---

## Common Mistakes to Avoid

1. **Shrinking too much or too little** — in dynamic window, ensure the loop that moves `left` stops as soon as the window is valid again.
2. **Off-by-one on length** — use `right - left + 1` for inclusive length; check bounds when `right < k - 1` in fixed window.
3. **Updating state too late** — update frequency/counts when expanding and when shrinking so the window state is always correct.
4. **Using sliding window when it doesn’t fit** — the condition must be maintainable by expanding/shrinking one element at a time; if not, consider two pointers or prefix sums.

---

## Real-World Examples

### Video streaming buffering
- The “window” is the buffered segment of the stream (e.g. next k seconds).
- As playback advances, the window slides: drop played data, add newly buffered data.
- Similar idea: fixed or rolling window over a stream of packets or frames.

### Network / rate limiting
- “At most N requests per window of T seconds” uses a time-based sliding window (or fixed windows) over request timestamps.

### Log and event analysis
- “Count distinct users in the last k minutes” or “max throughput in last hour” — sliding time windows over logs/events.

---

## Practice Problems (by difficulty)

### Easy
- Maximum Average Subarray I (fixed window)
- Contains Duplicate II (window of size k)
- Minimum Size Subarray Sum (dynamic window)
- Max Consecutive Ones III (dynamic, at most k flips)

### Medium
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Permutation in String (fixed window + frequency)
- Subarray Product Less Than K
- Max Consecutive Ones III
- Fruit Into Baskets (at most 2 types → k distinct)

### Hard
- Minimum Window Substring
- Sliding Window Maximum (deque / monotonic queue)
- Substring with Concatenation of All Words
