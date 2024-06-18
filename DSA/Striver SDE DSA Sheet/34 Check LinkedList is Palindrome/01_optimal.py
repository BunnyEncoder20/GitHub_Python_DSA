from typing import Optional

# Definition for singly-linked list.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[Node]) -> bool:
        if head is None or head.next is None : return True

        middle_node = self.get_mid(head)
        second_head = self.reverse_ll(middle_node.next) # reverse the ll after the middle node

        first = head
        second = second_head

        while second != None:
            if first.data != second.data :
                self.reverse_ll(second_head)    # in interviews, always return with the original data 
                return False
            
            first = first.next 
            second = second.next
        
        # If no mismatch found it is a palindrome
        self.reverse_ll(second_head)
        return True


    def get_mid(self,head):
        slow,fast = head,head 
        while fast.next != None and fast.next.next != None:
            slow = slow.next 
            fast = fast.next.next
        
        return slow

    def reverse_ll(self,head):
        if head is None or head.next is None: return head

        temp = head 
        prev = None

        while temp != None:
            next = temp.next
            temp.next = prev 
            prev = temp 
            temp = next
        
        return prev

    
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