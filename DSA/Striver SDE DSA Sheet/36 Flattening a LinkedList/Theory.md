# Flattening a LinkedList 

- Given a Linked List of size n, where every node represents a sub-linked-list and contains two pointers:
    - (i) a next pointer to the next node,
    - (ii) a bottom pointer to a linked list where this node is head.
- Each of the sub-linked-list is in sorted order.
- Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 

**Note:** The flattened list will be printed using the bottom pointer instead of the next pointer.

<br>

## Brute Force Approach 

### Algorithm 
- [Watch it here](https://youtu.be/ykelywHJWLg?si=UDLsy1GVVIr-X2bF&t=212)
- Convert the LinkedList into a array
- Sort the array 
- Convert the arry back into a LinkedList and return it.

<br>

### Code 
```python
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
```
- **Time complexity : O(x) + O(xlog(x)) + O(x) = 2xO(x) + O(xlog(x))** 
  - Where x = m*n
  - m = len(linkedlist)
  - n = len(child)
- **Space Complexity : 2xO(x)** (for the arr and the answer linkedlist)

<br>

## Optimal Approach

### Algorithm 
- [Watch it here](https://youtu.be/ykelywHJWLg?si=4OWQ21jFrJ3jMbeb&t=758)
- We take into consideration that the Child (vertical) nodes are sorted and we can do in-place changes by manipulating the links of the linkedlist (to save on space)
- pre-requesite : **Merging 2 sorted LinkedLists**

<br>

### Code 

```python 
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
```
- **Time Complexity : O(n x 2m) = O(2nm)** (assuming n is horizontal length and m is vertical depth)
- **Space Complexity : O(N)** (stack space)