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