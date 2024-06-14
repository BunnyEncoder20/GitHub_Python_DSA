# Actual Problem Code
def kReverse(head,k):
    temp = head 
    prev_group_node = None

    while temp != None :
        kth_node = getKth(temp,k)
        
        # The number of nodes remaining are less than k
        if kth_node == None : 
            if prev_group_node:
                prev_group_node.next = temp
            break

        # Saving the next_group starting node
        next_group_node = kth_node.next

        # seperating the current group from the remaining LL
        kth_node.next = None

        reverseLL(temp)
        printLinkedList(temp)

        # if it is the first group, reassign the new head 
        # else join the current group to the prev group
        if temp == head : 
            head = kth_node
        else :
            prev_group_node.next = temp 
        
        prev_group_node = temp
        temp = next_group_node
    
    return head


def getKth(temp,k):
    while k != None and k>1:
        k-=1
        temp = temp.next
    return temp

def reverseLL(head):
    back = Node(None)
    current = head 
    front = head.next

    while current != None:
        front = current.next
        current.next = back
        back = current 
        current = front

    return back     

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
head = kReverse(head,3)

# Print the reversed linked list
print("Reversed Linked List: ", end="")
printLinkedList(head)