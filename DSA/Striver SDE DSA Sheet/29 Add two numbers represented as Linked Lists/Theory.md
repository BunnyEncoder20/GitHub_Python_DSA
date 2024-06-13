# Add two numbers represented as Linked Lists

**Problem Statement:** You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

**Explain 1:**
> Input: l1 = [2,4,3], l2 = [5,6,4]
> Output: [7,0,8]
> Explanation: 342 + 465 = 807.

**Example 2:**
> Input: l1 = [0], l2 = [0]
> Output: [0]

**Example 3:**
> Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
> Output: [8,9,9,9,0,0,0,1]

<br>

## Optimal Approach

- There is only optimal approach in this question.
- hence ask the interviewer questions to not make it obivious that you know the question
- try to figure the edge cases like 
    - what if first is longer than the second 
    - what if second is longer than the first
    - what if they're equal, etc

<br> 

### Algorithm

1. [Watch it here](https://youtu.be/LBVsXSMOIk4?si=RhAJfd82E-C_KOhm&t=133)
2. Create a `dummy` node (gives the head of the linkedlist)
3. Create a `temp` pointer, pointing at `dummy`
5. Add the 2 elements of linkedlist to `sum` and if there is any `carry`, add that too. Rememeber that:
    - **sum = sum%10**
    - **carry = sum/10**
6. create a new node and put the sum%10 value in that. 
7. Make `temp` point to this new node. Move `temp` to the new node

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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pointer = dummy 
        carry = 0

        while (l1!=None or l2!=None) or carry:
            sum = 0 
            if l1.data:
                sum+=l1.data
                l1 = l1.next
            if l2.data:
                sum+=l2.data
                l2 = l2.next
            sum += carry
            carry = sum//10

            node = ListNode(sum%10)
            pointer.next = node 
            pointer = pointer.next 
        
        return dummy.next
            
    def printLL(self,head):
        pointer = head 
        while pointer != None:
            print(pointer.data, end=" ")
            pointer = pointer.next
        print()

if __name__ == "__main__":
    i = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)  # 342
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)  # 465

    head = i.addTwoNumbers(l1,l2)  
    i.printLL(head)                 # 807
```
- **Time complexity : O(max(n1,n2))** (n1,n2 are length of linkedlists)
- **Space complexity : O(n)** (len(summation))
