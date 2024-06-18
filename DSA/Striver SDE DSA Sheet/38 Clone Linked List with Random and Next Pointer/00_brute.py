# Node class to represent elements in the linked list
class Node:
    def __init__(self, x, nextNode=None, randomNode=None):
        self.data = x
        self.next = nextNode
        self.random = randomNode

# Actual Problem Code 
def cloneLL(head):
    temp = head
    hashmap = {}
    
    while temp :
        copied_node = Node(temp.data)
        hashmap[temp] = copied_node
        temp = temp.next
    
    temp = head 
    while temp:
        copied_node = hashmap[temp]
        copied_node.next = temp.next
        copied_node.random = temp.random
        temp = temp.next
    
    return hashmap[head]
        

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