from typing import Optional

# Definition for singly-linked list.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[Node]) -> bool:
        stack = []
        pointer = head 
        while pointer != None :
            stack.append(pointer.data)
            pointer = pointer.next 
        
        pointer = head 
        while pointer != None :
            top = stack.pop()
            if pointer.data != top:
                return False
            pointer = pointer.next 
        
        return True
    
    # Function to print the linked list
    def print_linked_list(self,head):
        temp = head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    i = Solution()
    # Create a linked list with
    # values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    i.print_linked_list(head)

    # Check if the linked list is a palindrome
    if i.isPalindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")