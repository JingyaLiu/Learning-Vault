# Fast and Slow Pointer (Floyd's Algorithm)

## Core Concept
The fast-slow pointer technique uses two pointers that traverse a linked list (or sequence) at different speeds. The slow pointer moves one step at a time; the fast pointer moves two steps at a time. As long as the fast pointer advances more steps than the slow pointer, the logic of the technique still applies.

**Key Insight:** When a fast pointer moves at 2× (or any greater multiple of) the slow pointer’s speed, they will eventually meet if there is a cycle. If there is no cycle, the fast pointer reaches the end first. This gives O(n) time and O(1) space for cycle detection and related problems.

---

## How It Works

### Pointer Movement
- **Slow pointer:** advances one step per iteration (`slow = slow.next`)
- **Fast pointer:** advances two steps per iteration (`fast = fast.next.next`)
- The ratio can vary (e.g., slow +1, fast +2) as long as the fast pointer gains on the slow one

### Visualization (cycle detection)
```
No cycle:
head → [1] → [2] → [3] → [4] → None
        S     F
             S          F
                  S               F (fast reaches None)

With cycle:
head → [1] → [2] → [3] → [4]
              ↑______________|
        S,F
             S     F
                  S     F  (they meet → cycle exists)
```

---

## When to Use Fast-Slow Pointers

### Problem Indicators
- **Cycle** — detect or analyze a cycle in a linked list (or similar structure)
- **Middle element** — find the middle node without knowing length
- **N-th from end** — find or remove the k-th node from the end
- **Cycle start** — find the node where the cycle begins
- **Palindrome linked list** — check if a list is a palindrome in O(n) time and O(1) space

### Required Conditions
1. **Linked list or sequence** — typically singly linked lists
2. **Linear traversal** — you can move one or two steps at a time
3. **O(1) extra space** — same spirit as two-pointer techniques

---

## Complexity Analysis

| Problem type       | Time  | Space |
|--------------------|-------|-------|
| Cycle detection    | O(n)  | O(1)  |
| Find middle        | O(n)  | O(1)  |
| Find cycle start   | O(n)  | O(1)  |
| N-th from end      | O(n)  | O(1)  |

---

## Common Patterns & Templates

### Pattern 1: Cycle Detection
```python
def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False
```

### Pattern 2: Find Middle Node
```python
def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # for even length, returns second middle
```

### Pattern 3: Find Start of Cycle
```python
def detect_cycle_start(head):
    if not head or not head.next:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # cycle found; reset slow to head
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None
```

### Pattern 4: Remove N-th Node from End
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next
```

---

## Common Mistakes to Avoid

1. **Null checks** — always check `fast` and `fast.next` before `fast.next.next` to avoid `AttributeError`
2. **Starting positions** — for cycle detection, some versions use `slow = head, fast = head.next`; be consistent with your invariants
3. **Off-by-one in “middle”** — for even length, clarify whether you want the first or second middle node
4. **Forgetting the dummy** — when removing the N-th from end, a dummy node simplifies handling the head

---

## Real-World Examples

### Detecting cycles in symlinks
- File systems: symbolic links can point to each other and form cycles
- Cycle detection (e.g., fast-slow pointer idea) is used to avoid infinite traversal when resolving symlink chains

### Tortoise and hare (Floyd’s algorithm)
- Classic formulation for cycle detection and cycle start in linked structures
- Same idea appears in pseudo-random number generators and other state-machine cycle detection

---

## Practice Problems (by difficulty)

### Easy
- Linked List Cycle
- Middle of the Linked List
- Palindrome Linked List
- Remove Nth Node From End of List

### Medium
- Linked List Cycle II (find cycle start)
- Reorder List (middle + reverse + merge)
- Remove Duplicates from Sorted List II

### Hard
- Find the Duplicate Number (array variant using indices as “next” pointers)
- Copy List with Random Pointer (can combine with cycle-style traversal)
