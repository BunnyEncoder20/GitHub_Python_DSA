# Clone Linked List with Random and Next Pointer

- Problem Statement: Given a linked list where every node in the linked list contains two pointers:
    - `next` which points to the next node in the list.
    - `random` which points to a random node in the list or `null`.
- Create a ‘deep copy’ of the given linked list and return it. 

<br>

## Brute Force Approach 

### Algorithm

- [Watch it here](https://youtu.be/q570bKdrnlw?si=2yVsZt6El3DsYxmB&t=99)
- First we need to craete all the nodes first (cause of the random pointer)
- temp pointing at head
- resultant pointing at dummy_node
- copy the nodes from temp to result and move them to the next node (remember the resultant is not connecting the nodes in this step).
- We also need to remember the nodes is a hashmap(original_node, copied_node)
- In second pass, we link all the copied nodes to thier next nodes and also link the random links.

### Code 

```python
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
```

- **Time complexity : O(n)+O(n) = O(2n)** (both of the while loops)
- **Space complexity : O(n) + O(n)** (hashmap + answer ll)

<br>

## Optimal Approach 

- We can avoid using the hashmap by making the original nodes point to their copied nodes

### Algorithm

- [Watch it here](https://youtu.be/q570bKdrnlw?si=NDqdI95X1nbc-1SV&t=772)
- Temp pointing at head
- Insert the copy nodes in between the temp and temp.next
- move temp by 2 nodes (to get to the next original node)
- Reset temp and connect the random pointers 
- Connecting the next pointers using a dummy_ndoe (for the head), resultant and temp pointers

### Code 

```python
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
```

- **Time Complexity : O(n) + O(n) + O(n) = O(3n)**
- **Space Complexity : O(n)**