# Remove nth Node from Back of LinkedList

- Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

## Brute Force Approach 

### Algorithm 

0. [Watch it here](https://youtu.be/3kMKYQ2wNIU?si=iyoFZFBXP55xvN2O&t=68)
1. Count the number of nodes 
2. nth node from back will count-n
3. Change the link to point to the node.next.next

### Code

```python
from typing import Optional

class Node():
    def __init__(self,data=0,next=None):
        self.data = data 
        self.next = next

class Solution :
    def DeleteNthNodefromEnd(self, head: Optional[Node], N: int) -> Optional[Node]:
        node_count = 0
        pointer = head
        while pointer != None:
            node_count+=1
            pointer=pointer.next 
        
        # If the count = N , that means nth node from behind is going to be the head
        # In that case return the newhead
        if node_count == N:
            newhead = head.next
            head.next = None 
            return newhead

        nodes2traverse = node_count-N-1
        pointer=head 
        while nodes2traverse:
            pointer = pointer.next 
            nodes2traverse-=1
        
        deleteNode = pointer.next 
        pointer.next = pointer.next.next
        deleteNode = None 

        return head


    def printLL(self, head: Optional[Node]):
        pointer = head 
        while pointer!=None:
            print(pointer.data,end=" ")
            pointer = pointer.next
        print()

if __name__ == "__main__":
    i = Solution()
    arr = [1, 2, 3, 4, 5]
    N = 3
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    # printnig the original lsit 
    i.printLL(head)

    # Delete the Nth node from the end and print the modified linked list
    head = i.DeleteNthNodefromEnd(head, N)
    i.printLL(head)
```
- **Time complexity : O(len(n))+O(len(n)-N)**
- **Space complexity : O(1)** 

<br>

## Optimal Apporach 

### Algorithm 

- [Watch it here](https://youtu.be/3kMKYQ2wNIU?si=NratJWSQlJWz0O2h&t=573)
- Put fast pointer N steps ahead and slow pointer at head
- move them one by one, until fast_pointer is at last node
- Then slow_pointer is at node right before the node to be deleted. 

### Code 

```python 
from typing import Optional

class Node():
    def __init__(self,data=0,next=None):
        self.data = data 
        self.next = next

class Solution :
    def DeleteNthNodefromEnd(self, head: Optional[Node], N: int) -> Optional[Node]:
        fast_pointer = head
        for i in range(N):
            fast_pointer = fast_pointer.next 

        # Edge case : If N = len(linkedlist) then the fast_pointer will be at None
        if fast_pointer == None :
            deleteNode = head 
            newhead = head.next 
            return newhead 
        
        slow_pointer = head

        while fast_pointer.next != None:
            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next
        
        deleteNode = slow_pointer.next 
        slow_pointer.next = slow_pointer.next.next

        return head

    def printLL(self, head: Optional[Node]):
        pointer = head 
        while pointer!=None:
            print(pointer.data,end=" ")
            pointer = pointer.next
        print()

if __name__ == "__main__":
    i = Solution()
    arr = [1, 2, 3, 4, 5]
    N = 5
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    # printnig the original lsit 
    i.printLL(head)

    # Delete the Nth node from the end and print the modified linked list
    head = i.DeleteNthNodefromEnd(head, N)
    i.printLL(head)
```
- **Time complexity : O(len(n))**
- **Space complexity : O(1)**