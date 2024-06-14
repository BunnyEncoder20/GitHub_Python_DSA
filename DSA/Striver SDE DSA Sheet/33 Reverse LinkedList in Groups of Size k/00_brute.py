# Actual Problem Code
def kReverse(head, k):
    pass

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a linked list with
# values 5, 4, 3, 7, 9 and 2
head = Node(5)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(7)
head.next.next.next.next = Node(9)
head.next.next.next.next.next = Node(2)

# Print the original linked list
print("Original Linked List: ", end="")
printLinkedList(head)

# Reverse the linked list
head = kReverse(head, 4)

# Print the reversed linked list
print("Reversed Linked List: ", end="")
printLinkedList(head)