# Node class to represent elements in the linked list
class Node:
    def __init__(self, x, nextNode=None, randomNode=None):
        self.data = x
        self.next = nextNode
        self.random = randomNode

# Actual Problem Code 
def cloneLL(head):
    
    # 1. inserting the copied in between the original nodes
    temp = head
    while temp != None: 
        copy_node = Node(temp.data)
        copy_node.next = temp.next
        temp.next = copy_node
        temp = temp.next.next
    
    # 2 connecting the copy's random pointers to random nodes copy
    temp = head
    while temp != None:
        copy_node = temp.next
        if temp.random != None:
            copy_node.random = temp.random.next
        else:
            copy_node.randnom = None
        temp = temp.next.next
    
    # 3 Connecting the next pointers and extracting the copy list 
    temp = head
    dummy = Node(-1)
    resultant = dummy
    
    while temp != None :
        resultant.next = temp.next
        temp.next = temp.next.next
        
        resultant = resultant.next
        temp = temp.next
    
    return dummy.next
        
        

# Function to print the cloned linked list
def printClonedLinkedList(head):
    while head is not None:
        print(f"Data: {head.data}", end="")
        if head.random is not None:
            print(f", Random: {head.random.data}")
        else:
            print(", Random: nullptr")
        head = head.next

# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    print("Original Linked List with Random Pointers:")
    printClonedLinkedList(head)

    # Clone the linked list
    clonedList = cloneLL(head)

    print("\nCloned Linked List with Random Pointers:")
    printClonedLinkedList(clonedList)