class Node:
    def __init__(self, x=None, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode

def merge2lists(list1,list2):
    dummy_node = Node(None)
    resultant = dummy_node

    while list1 != None and list2 != None :
        if list1.data <= list2.data:
            resultant.child = list1 
            resultant = list1 
            list1 = list1.child
        else:
            resultant.child = list2 
            resultant = list2 
            list2 = list2.child
        resultant.next = None
    
    if list1 : resultant.child = list1
    else : resultant.child = list2

    return dummy_node.child
    

def flattenLinkedList(head):
    # Base case 
    if head == None or head.next == None : 
        return head 

    # Rest case : keep going till we reach the last node 
    next_head = flattenLinkedList(head.next)

    # Merge the current head and the next head
    merged_head = merge2lists(head,next_head)

    # return the merged list head
    return merged_head

# Print the linked list by
# traversing through child pointers
def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.child
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
head.child = Node(7)
head.child.child = Node(8)
head.child.child.child = Node(30)

head.next = Node(10)
head.next.child = Node(20)

head.next.next = Node(19)
head.next.next.child = Node(22)
head.next.next.child.child = Node(50)

head.next.next.next = Node(28)
head.next.next.next.child = Node(35)
head.next.next.next.child.child = Node(40)
head.next.next.next.child.child.child = Node(45)

# Print the original
# linked list structure
print("Original linked list:")
printOriginalLinkedList(head)

# Flatten the linked list
# and print the flattened list
flattened = flattenLinkedList(head)
print("\nFlattened linked list: ")
printLinkedList(flattened)