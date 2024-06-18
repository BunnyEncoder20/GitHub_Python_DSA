# Reversing a LinkedList 

## Brute Approach

### Algorithm 

- [Watch it here](https://youtu.be/D2vI2DNJGd8?si=e4ukfCIzGez4YejF&t=33)
- Use a stack to store the elements 
- Pop em out in reverse order and populate the LL

<br>

### Code 

```python
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        # 1. Push every element into the stack
        temp = head
        while temp != None :
            stack.append(temp.data)
            temp = temp.next 
        
        # 2. Pop every element back into the LL
        temp = head 
        while temp != None :
            temp.data = stack.pop()
            temp = temp.next
        
        return head

    def printLinkedList(self,head):
        pointer = head
        print("None",end="")
        while pointer != None :
            print(" <- ",pointer.data, end="")
            pointer = pointer.next
        print()

if __name__ == "__main__":
    # Create a linked list with
    # values 1, 2, 3, 4 and 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    i = Solution()

    i.printLinkedList(head)
    reverse_head = i.reverseList(head)
    i.printLinkedList(reverse_head)
```
- **Time complexity : O(2n)**
- **Space complexity : O(n)**

<br>

## Better Approach (Iterative)

- We can improve on the space complexity by not using th stack and directly altering the next links.

### Algorithm 

- [Watch it here](https://youtu.be/D2vI2DNJGd8?si=VFgMXcn_k_HNe0yZ&t=308)
- Create a dummy node
- make a head pointer and a next pointer 
- make next pointer point to head.next()
- make head pointer to point to dummy node
- Increment the pointers such that 
    - dummy is at head,
    - head is at next,
- Update next pointer
- Update head pointer 

<br>

### Code

```python 
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(None,None)
        current = head 
        next = head.next

        while current != None : 
            next = current.next 
            current.next = prev 
            prev = current 
            current = next
        # prev will the be pointing to the new head of our LL
        return prev


    def printLinkedList(self,head):
        pointer = head 
        print("None",end="")
        while pointer != None : 
            print(" <- ",pointer.data,end="")
            pointer = pointer.next
        print()


if __name__ == "__main__":
    # Create a linked list with
    # values 1, 3, 2, and 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    i = Solution()

    i.printLinkedList(head)
    reverse_head = i.reverseList(head)
    i.printLinkedList(reverse_head)

```
- **Time Complexity : O(n)**
- **Space Complexity : O(1)**

<br>

## Better Approach (Recursive)

### Algorithm 
- [Watch it here](https://youtu.be/D2vI2DNJGd8?si=iUaR2_lQJU7ZNkfZ&t=982)

### Code 

```python
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def reverse_linkedlist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        
        new_head = self.reverse_linkedlist(head.next)
        front = head.next

        front.next = head
        head.next = None

        return new_head


    def printLinkedList(self,head):
        pointer = head 
        print("None",end="")
        while pointer != None : 
            print(" <- ",pointer.data,end="")
            pointer = pointer.next
        print()


if __name__ == "__main__":
    # Create a linked list with
    # values 1, 3, 2, and 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    i = Solution()

    i.printLinkedList(head)
    reverse_head = i.reverse_linkedlist(head)
    i.printLinkedList(reverse_head)
```
- **Time complexity : O(n)**
- **Space complexity : O(1)** 