from typing import Optional

# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def intersectionPresent(self, headA: Node, headB: Node) -> Optional[Node]:
        p1 = headA

        while p1 != None:
            p2 = headB
            while p2 != None:
                if p1 == p2 :
                    return p2
                p2 = p2.next
            p1 = p1.next
            
        return None

    # utility function to insert node at the end of the linked list
    def insertNode(self,head, val):
        newNode = Node(val)
        if head == None:
            head = newNode
            return head
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        return head

    # utility function to print the Linkedlists
    def printLL(self,head):
        pointer = head 
        while pointer != None:
            print(pointer.val, end=" ")
            pointer = pointer.next
        print()

if __name__ == '__main__':
    i = Solution()

    head = None
    head = i.insertNode(head, 1)
    head = i.insertNode(head, 3)
    head = i.insertNode(head, 1)
    head = i.insertNode(head, 2)
    head = i.insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = i.insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head

    print('List1: ', end='')
    i.printLL(head1)
    print('List2: ', end='')
    i.printLL(head2)

    answerNode = i.intersectionPresent(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val)
    