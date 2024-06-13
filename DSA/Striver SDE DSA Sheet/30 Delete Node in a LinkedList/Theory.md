# Delete Node in a LinkedList 

- There is a singly-linked list `head` and we want to delete a node node in it.
- You are given the node to be deleted node. You will not be given access to the first node of head.
- All the values of the linked list are unique, and it is guaranteed that the given node is **not the last node** in the linked list.
- Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:
    - The value of the given node should not exist in the linked list.
    - The number of nodes in the linked list should decrease by one.
    - All the values before node should be in the same order.

<br>

## The only Approach 

### Algorithm 

1. We indirectly delete the node
1. Copy the deleteNode.next value into the deleteNode
2. Update the deleteNode to point to next.next

<br>

### Code

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.data = node.next.data
        node.next = node.next.next
    
    def printLL(self,head):
        pointer = head 
        while pointer != None:
            print(pointer.data, end=" ")
            pointer = pointer.next
        print()

if __name__ == "__main__":
    i=Solution()
    ll = ListNode(1)
    ll.next = ListNode(4)
    ll.next.next = ListNode(2)
    ll.next.next.next = ListNode(3)
    delNode = ll.next.next
    i.printLL(ll)
    i.deleteNode(delNode)
    i.printLL(ll)
```
- **Time complexty : O(1)**
- **Space complexity : O(1)**