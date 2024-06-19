class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Actual Solution Code 
def rotateRight(head,k):
    if head is None or head.next is None or k==0 : return head

    # calc length of ll
    pointer = head
    length = 1
    while pointer.next:
        length+=1
        pointer = pointer.next

    # Calc required k
    required_k = k % length
    # connect last node to head 
    pointer.next = head 
    # calc end index
    end = length-required_k

    # get to the end node
    pointer = head 
    for i in range(end-1):
        pointer = pointer.next
    head = pointer.next
    pointer.next = None

    return head
    

# utility function to print list
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)
    return

# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head


if __name__ == '__main__':
    head = None
    # inserting Node
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 5)

    print("Original list: ", end='')
    printList(head)

    k = 2
    # calling function for rotating right of the nodes by k times
    newHead = rotateRight(head, k)

    print("After", k, "iterations: ", end='')
    printList(newHead)  # list after rotating nodes