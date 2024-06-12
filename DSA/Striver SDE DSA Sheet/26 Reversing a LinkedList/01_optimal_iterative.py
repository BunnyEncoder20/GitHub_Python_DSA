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
