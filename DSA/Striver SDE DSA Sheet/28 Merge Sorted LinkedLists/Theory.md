# Merge Two Sorted LinkedLists

- You are given the heads of two sorted linked lists `list1` and `list2`.
- Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
- Return the head of the merged linked list.

<br>

## Brute Force Approach 

### Algorithm

- Take out all of the elements of L1 and L2 into a array
- Sort the array. 
- Convert it back into linkedlist
- Return the head of the linkedlist 

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

```
- **Time Complexity : O(n1)+O(n2)+O(nlogn)+O(n)** 
- **Space Complexity : O(n1)+O(n2)** (array + linkedlist)

<br>

## Optimal Approach 

- Use the sorted and 2 pointer approach
- Whenever we manipulate the links of a linkedlist, we always use the concept of dummy nodes
- Hence we can save on the time complexity (using sorted) and space complexity (using same nodes)

### Algorithm

- [Watch it here](https://youtu.be/jXu-H7XuClE?si=L61P1ltqJ1UxWbnt&t=473)
- Start with a dummy node and reassign all the links

### Code 

```python 
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
```
- **Time complexity : O(n1+n2)**
- **Space complexity : O(1)** (cause reused nodes)