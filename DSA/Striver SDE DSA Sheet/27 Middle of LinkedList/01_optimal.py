from typing import Optional

# Definition for singly-linked list.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def middleNode(self, head: Optional[Node]) -> Optional[Node]:
        slow = Node()
        fast = Node()
        
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next
        
        return slow
    

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Find the middle node
    i = Solution()
    middle_node = i.middleNode(head)

    # Display the value of the middle node
    print("The middle node value is:", middle_node.data)