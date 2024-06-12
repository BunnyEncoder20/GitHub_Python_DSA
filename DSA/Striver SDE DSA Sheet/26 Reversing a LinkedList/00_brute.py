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
