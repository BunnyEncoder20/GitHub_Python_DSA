class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Actual Solution Code 
def rotateRight(head,k):
    if head is None or head.next is None : return head

    # for k times , move the last node to the front
    for i in range(k):
        temp = head
        # reach the second last node
        while temp.next.next != None:
            temp = temp.next
        end = temp.next
        temp.next = None
        end.next = head 
        head = end
    
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