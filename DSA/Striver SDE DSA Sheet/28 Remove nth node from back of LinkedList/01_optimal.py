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