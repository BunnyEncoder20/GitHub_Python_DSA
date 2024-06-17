class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

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


# utility function to print linked list created
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)
    


# Actual question code here 
def intersectionPresent(head1,head2):
    if head1 == None or head2 == None: return None
        
    dummy1 = head1
    dummy2 = head2
    
    while dummy1 != dummy2:
        if dummy1 == None: dummy1 = head2
        else : dummy1 = dummy1.next
        
        if dummy2 == None : dummy2 = head1
        else : dummy2 = dummy2.next
    
    return dummy2
    

if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = intersectionPresent(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val)