# Check if LinkedList is Palindrome

- Given the `head` of a singly linked list, return `true` if it is a 
palindrome or `false` otherwise.

<br>

## Brute Force Approach 

### Algorithm 

- [Watch it here](https://youtu.be/lRY_G-u_8jk?si=lFBUZ6xBbNAnOYWY&t=119)
- Take a stack
- Use a temp pointer insert values into the stack 
- Reset the temp to head and compare it to the popped out values of the Stack (cause stack is LIFO)

<br>

### Code  

```python 
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
```
- **Time Complexity : O(2n)**
- **Space Complexity : O(n)**

<br>

## Optimal Approach 

- We can improve the space complexity by reversing the links of the second half of the linkedlist
- We will need both `find_mid_of_ll(head)` and `reverse_ll()` functions
- once the ll is reversed from the mid, compare with 2 pointers.

<br>

### Code 

```python 
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
```

- **Time Complexity : O(2n)**
- **Space Complexity : O(1)**