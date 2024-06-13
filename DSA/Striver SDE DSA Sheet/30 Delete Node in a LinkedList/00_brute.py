
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