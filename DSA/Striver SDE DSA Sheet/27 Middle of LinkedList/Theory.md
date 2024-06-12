# Finding the Middle of a LinkedList 

- Given the `head` of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

<br>

## Brute Force Approach 

### Algorithm
- [Watch it here](https://youtu.be/7LjQ57RqgEc?si=dYJq_AE6p99Mq9p8&t=84)
- count the number of nodes
- middle = (n//2) + 1

### Code 

```python
from typing import Optional

# Definition for singly-linked list.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def middleNode(self, head: Optional[Node]) -> Optional[Node]:
        pointer = head
        node_count = 0
        
        while pointer != None: 
            node_count+=1
            pointer = pointer.next
        print(node_count)
        middle = node_count//2
        print(middle)
        
        pointer = head
        while middle>0 : 
            pointer = pointer.next 
            middle-=1
        
        return pointer
            

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Find the middle node
    i = Solution()
    middle_node = i.middleNode(head)

    # Display the value of the middle node
    print("The middle node value is:", middle_node.data)
```
- **Time complexity : O(n + n/2)**
- **Space complexity : O(1)**

<br>

## Better Approach

- Optimal approach will find the middle element in one pass

### Algorithm

- using tortoise and hare algorithm
- The moment the fast pointer reaches the last node, we stop.
- The smaller pointer will be the middle node. 

<br>

### Code

```python

```
- Time complexity : O(n)
- Space complexity : O(1)