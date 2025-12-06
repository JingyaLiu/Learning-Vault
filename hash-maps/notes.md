# Hash Maps & Hash Sets

## Core Concept
Hash maps (also called hash tables or dictionaries) are data structures that pair keys with values, enabling quick access to information. They store key-value pairs with no duplicate keys and are typically unordered. Hash maps excel at lookups, insertions, and deletions, typically performing these operations in **constant time O(1)** average case.

**Key Insight:** Hash maps trade space for time—they use extra memory to achieve fast O(1) average-case operations, making them ideal when you need frequent lookups or need to track relationships between data.

---

## Hash Maps vs Hash Sets

### Hash Maps (Dictionary/Map)
- Stores **key-value pairs**
- Each key maps to a value
- No duplicate keys (duplicate values are allowed)
- **Use cases:**
  - Counting the frequency of elements
  - Caching data (memoization)
  - Storing key-value relationships
  - Quick lookup by key
  - Grouping elements by a property

### Hash Sets
- Stores **only keys** (no values)
- Stores unique elements only
- **Use cases:**
  - Storing unique elements
  - Marking elements as used or visited
  - Checking for duplicates
  - Fast membership testing (is element present?)

---

## When to Use Hash Maps

### Problem Indicators
Pay attention to these keywords in problem descriptions:
- **Frequency** — counting occurrences
- **Unique** — tracking distinct elements
- **Map/Dictionary** — explicit mention
- **Fast lookup** — need O(1) access
- **Grouping** — organizing data by a property
- **Complement/Pair** — finding matching elements (e.g., two sum)

### Common Problem Patterns
1. **Frequency counting** — count occurrences of elements
2. **Two sum variants** — finding pairs that sum to target
3. **Grouping** — grouping elements by a common property
4. **Caching/memoization** — storing computed results
5. **Tracking state** — marking visited nodes, tracking seen elements
6. **Index mapping** — mapping values to their indices

---

## Complexity Analysis

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert    | O(1)         | O(n)       |
| Lookup    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |
| Space     | O(n)         | O(n)       |

**Note:** Worst case occurs when all keys hash to the same bucket (rare with good hash functions).

---

## Hash Function Fundamentals

### How Hash Functions Work
Hash functions map keys to specific indices in the hash table. A good hash function:
- Distributes keys uniformly across buckets
- Is deterministic (same key → same hash)
- Is fast to compute
- Minimizes collisions

### Collisions
When two different keys hash to the same index, a collision occurs.

**Collision Handling Techniques:**

1. **Chaining (Separate Chaining)**
   - Each bucket contains a linked list (or array) of key-value pairs
   - When collision occurs, add to the list
   - Lookup: hash to bucket, then search the list
   - **Pros:** Simple, handles many collisions
   - **Cons:** Extra memory for pointers, cache performance

2. **Open Addressing**
   - Store key-value pairs directly in the table
   - When collision occurs, find next available slot using probing:
     - **Linear probing:** next slot (i+1, i+2, ...)
     - **Quadratic probing:** (i+1², i+2², ...)
     - **Double hashing:** use second hash function
   - **Pros:** Better cache performance, no extra pointers
   - **Cons:** More complex, clustering issues

### Load Factor and Rehashing
- **Load factor** = number of elements / number of buckets
- When load factor exceeds threshold (typically 0.75), table is resized (rehashed)
- Rehashing: create larger table, rehash all elements
- Keeps operations efficient by maintaining low load factor

---

## Common Patterns & Templates

### Pattern 1: Frequency Counting
```python
def count_frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq
```

### Pattern 2: Two Sum (Hash Map Approach)
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Pattern 3: Grouping Elements
```python
def group_by_key(items, key_func):
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups
```

### Pattern 4: Tracking Visited/Seen Elements
```python
def has_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
```

---

## Common Mistakes to Avoid

1. **Assuming O(1) worst case** — hash maps are O(1) average case, O(n) worst case
2. **Forgetting to check existence** — use `.get()` or `in` operator before accessing
3. **Mutable keys** — don't use mutable objects (lists, dicts) as keys
4. **Not handling edge cases** — empty inputs, single element, all duplicates
5. **Overusing hash maps** — sometimes arrays or sets are sufficient

---

## Real-World Examples

### Web Browser Cache
- Maps URLs to cached web pages
- Fast lookup when user revisits a page
- Eviction policies (LRU) when cache is full

### Database Indexing
- Hash indexes for fast record lookup
- Maps search keys to record locations

### Symbol Tables (Compilers)
- Maps variable names to their types/values
- Fast lookup during compilation

---

## Practice Problems (by difficulty)

### Easy
- Two Sum
- Contains Duplicate
- Valid Anagram
- First Unique Character in String

### Medium
- Group Anagrams
- Longest Substring Without Repeating Characters
- Top K Frequent Elements
- Design HashMap (implement from scratch)

### Hard
- LRU Cache
- Design Twitter
- Word Ladder II