# Rotating a LinkedList 

- Given the `head` of a linked list, rotate the list to the right by `k` places.

## Brute Force Approach 

### Algorithm 

- [Watch it here](https://youtu.be/9VPm6nEbVPA?si=6RHC9n1XuJeVChvr&t=92)
- Pick up the last node and put it at the front for K times 

<br>

### Code 

```python
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
```
- **Time Complexity : O(Number of nodes present in the list*k)**
- **Space Complexity : O(1)**

<br>

## Optimal Approach 

- Any rotations which are multiple of len(ll), will result in the same ll.

### Algorithm 

- [Watch it here](https://youtu.be/9VPm6nEbVPA?si=clWNeSEngNHGXbFa&t=242)
- When `k>len(ll)` then **k = k%len(ll)**
- Hence compute the length of ll and find actual `k`
- **end node = len(ll)-k** node from start.
- make the `head = end_node.next` and `end_node.next = None`

<br>

### Code

```python 
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
```
- **Time complexity : O(n) + O(n - n%k) = O(n)**
- **Space complexity : O(1)**