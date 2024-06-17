from typing import Optional

# Definition for singly-linked list.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def sort_two_linked_lists(self, head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
        pointer1 = head1
        pointer2 = head2
        
        dummyNode = Node(-1)
        temp = dummyNode
        
        while pointer1 != None and pointer2 != None : 
            if pointer1.data <= pointer2.data :
                temp.next = pointer1
                temp = pointer1
                pointer1 = pointer1.next
            else :
                temp.next = pointer2
                temp = pointer2
                pointer2 = pointer2.next
        
        # If either of ll have some elements in them
        if pointer1 : temp.next = pointer1
        else : temp.next = pointer2
        
        return dummyNode.next 

    def print_linked_list(self,head):
        temp = head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    list1 = Node(1)
    list1.next = Node(3)
    list1.next.next = Node(5)

    list2 = Node(2)
    list2.next = Node(4)
    list2.next.next = Node(6)
    
    i = Solution()

    print("First sorted linked list: ", end="")
    i.print_linked_list(list1)

    print("Second sorted linked list: ", end="")
    i.print_linked_list(list2)

    merged_list = i.sort_two_linked_lists(list1, list2)

    print("Merged sorted linked list: ", end="")
    i.print_linked_list(merged_list)