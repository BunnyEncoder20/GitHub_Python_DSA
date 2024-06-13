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