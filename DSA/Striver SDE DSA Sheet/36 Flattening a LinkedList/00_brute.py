class Node:
    def __init__(self, x=None, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode

# Function to convert a list to a linked list
def convertArrToLinkedList(arr):
    if len(arr)==0 : return None

    head = Node(arr[0])
    temp = head

    for node in arr[1:]:
        new_node = Node(node)
        temp.next = new_node
        temp = new_node
    
    return head

def flattenLinkedList(head):
    arr = []
    temp1 = head 

    # Making the linkedlist into a array
    # first loop for traversing the linkedlist nodes
    while temp1 != None :
        # second node  for traversing the child nodes        
        temp2 = temp1
        while temp2 != None :
            arr.append(temp2.data)
            temp2 = temp2.child
        temp1 = temp1.next

    arr.sort()

    return convertArrToLinkedList(arr)

# Print the linked list by
# traversing through child pointers
def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

# Print the linked list in a grid-like structure
def printOriginalLinkedList(head, depth=0):
    while head:
        print(head.data, end="")

        # If child exists, recursively
        # print it with indentation
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars
        # for each level in the grid
        if head.next:
            print()
            print("| " * depth, end="")

        head = head.next

# Create a linked list with child pointers
head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

# Print the original
# linked list structure
print("Original linked list:")
printOriginalLinkedList(head)

# Flatten the linked list
# and print the flattened list
flattened = flattenLinkedList(head)
print("\nFlattened linked list: ")
printLinkedList(flattened)