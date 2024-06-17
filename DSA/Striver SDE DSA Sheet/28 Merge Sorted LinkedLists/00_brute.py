from typing import Optional

# Definition for singly-linked list.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def sort_two_linked_lists(self, head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
        ans = []

        temp = head1
        while temp != None:
            ans.append(temp.data)
            temp = temp.next
        temp = head2
        while temp != None:
            ans.append(temp.data)
            temp = temp.next
        
        ans.sort()
        
        return self.convert2linkedlist(ans)
    
    def convert2linkedlist(self,arr):
        if not arr : return None
        
        head = Node(arr[0])
        current_node = head
        for element in arr[1:]:
            current_node.next = Node(element)
            current_node = current_node.next
        
        return head
    
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

