# Linked Lists

## Core Concept
A linked list is a sequence of nodes where each node contains two main components: the data it stores and a reference to the next node (and optionally the previous node) in the sequence.

**Key Insight:** Unlike arrays, linked lists don't store elements in contiguous memory. This allows for dynamic sizing and efficient insertions/deletions, but sacrifices random access capabilities.

---

## Node Definition

We typically define a node using a `ListNode` class:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## Types of Linked Lists

### 1. Singly Linked List
Each node points to the next node in the linked list, and the last node points to `None`, indicating the end of the linked list. The start of the linked list is called the `head`, which is generally the only node we initially have access to.

**Characteristics:**
- Unidirectional traversal (forward only)
- Each node has one pointer: `next`
- Last node's `next` is `None`

**Visualization:**
```
head → [val1|next] → [val2|next] → [val3|next] → None
```

**Advantages:**
- Dynamic sizing (can grow or shrink flexibly)
- Efficient insertions and deletions at any position (O(1) if we have a pointer to the node)
- No need to pre-allocate memory

**Disadvantages:**
- No random access (must traverse from head to reach a node)
- Extra memory overhead for storing pointers
- Cache performance is worse than arrays (nodes not in contiguous memory)

### 2. Doubly Linked List
Each node has two pointers: one to the next node and one to the previous node, enabling bidirectional traversal.

**Characteristics:**
- Bidirectional traversal (forward and backward)
- Each node has two pointers: `next` and `prev`
- First node's `prev` is `None`
- Last node's `next` is `None`

**Visualization:**
```
None ← [prev|val1|next] ↔ [prev|val2|next] ↔ [prev|val3|next] → None
```

**Advantages:**
- Can traverse in both directions
- Deleting a node in a doubly linked list is generally more straightforward (we have direct access to the previous node)
- Can delete a node in O(1) time if we have a pointer to it

**Disadvantages:**
- Extra memory overhead (two pointers per node)
- More complex implementation
- More pointer updates needed for insertions/deletions

---

## Complexity Analysis

| Operation | Singly Linked List | Doubly Linked List |
|-----------|-------------------|-------------------|
| Access by index | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(1)* | O(1)* |
| Insert at position | O(n) | O(n) |
| Delete at head | O(1) | O(1) |
| Delete at tail | O(n) | O(1) |
| Delete at position | O(n) | O(n) |
| Delete given node | O(n)** | O(1) |
| Space | O(n) | O(n) |

\* O(1) if we maintain a tail pointer, otherwise O(n) to find the tail  
\** O(n) to find the previous node, O(1) if we have a pointer to the previous node

---

## Common Patterns & Templates

### Pattern 1: Traversal
```python
def traverse(head):
    current = head
    while current:
        # Process current node
        print(current.val)
        current = current.next
```

### Pattern 2: Two Pointers (Fast and Slow)
Also known as Floyd's Cycle Detection Algorithm or the "tortoise and hare" approach.

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

**Use cases:**
- Detecting cycles in linked lists
- Finding the middle node
- Finding the k-th node from the end
- Finding the start of a cycle

### Pattern 3: Reversing a Linked List
```python
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev
```

### Pattern 4: Dummy Node Technique
Using a dummy node simplifies edge cases (empty list, single node, etc.).

```python
def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 if list1 else list2
    return dummy.next
```

### Pattern 5: Finding the Middle Node
```python
def find_middle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

### Pattern 6: Removing the N-th Node from End
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove the node
    second.next = second.next.next
    return dummy.next
```

### Pattern 7: Merging Two Sorted Lists
```python
def merge_two_sorted_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append remaining nodes
    current.next = list1 if list1 else list2
    return dummy.next
```

---

## When to Use Linked Lists

### Use Linked Lists When:
- You need frequent insertions/deletions at arbitrary positions
- The size of the data structure is unknown or changes frequently
- Memory allocation is a concern (can allocate nodes as needed)
- You're implementing stacks, queues, or other data structures
- You need to avoid memory reallocation overhead

### Prefer Arrays When:
- You need random access to elements
- You know the size in advance
- Memory usage is critical (arrays have less overhead)
- Cache performance matters (arrays have better locality)

---

## Common Mistakes to Avoid

1. **Losing the head reference** — Always maintain a reference to the head, or use a dummy node
2. **Null pointer exceptions** — Always check if `current` or `current.next` is `None` before accessing
3. **Forgetting to update pointers** — When inserting/deleting, make sure all relevant pointers are updated
4. **Off-by-one errors** — Be careful with loop conditions and pointer movements
5. **Not handling edge cases** — Empty list, single node, two nodes
6. **Memory leaks** — In languages without garbage collection, make sure to free deleted nodes
7. **Modifying the list while traversing** — Be careful when modifying a list you're currently iterating over

---

## Related Techniques

### Two Pointers on Linked Lists
- **Fast and Slow Pointers:** Used for cycle detection, finding middle, finding k-th from end
- **Multiple Pointers:** Used for complex operations like reversing portions of a list

### Recursion
Many linked list problems can be solved elegantly with recursion:
- Reversing a linked list
- Merging sorted lists
- Traversing and processing nodes

### Hash Sets
Use hash sets to:
- Detect cycles (store visited nodes)
- Remove duplicates
- Find intersection of two linked lists

---

## Practice Problems (by difficulty)

### Easy
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Remove Duplicates from Sorted List
- Middle of the Linked List
- Palindrome Linked List
- Remove Linked List Elements

### Medium
- Add Two Numbers
- Remove Nth Node From End of List
- Swap Nodes in Pairs
- Reverse Linked List II
- Partition List
- Rotate List
- Copy List with Random Pointer
- Intersection of Two Linked Lists
- Reorder List

### Hard
- Merge k Sorted Lists
- Reverse Nodes in k-Group
- LRU Cache (uses doubly linked list)
- LFU Cache
- Design Linked List (implement from scratch)

---

## Tips for Interview Problems

1. **Always draw diagrams** — Visualize the list structure and pointer movements
2. **Use dummy nodes** — They simplify edge cases and make code cleaner
3. **Two pointers are powerful** — Fast/slow pointers solve many problems
4. **Consider recursion** — Some problems are more elegant with recursion
5. **Handle edge cases first** — Empty list, single node, two nodes
6. **Test with examples** — Walk through your solution with a small example
7. **Watch for cycles** — Be careful not to create cycles unintentionally
