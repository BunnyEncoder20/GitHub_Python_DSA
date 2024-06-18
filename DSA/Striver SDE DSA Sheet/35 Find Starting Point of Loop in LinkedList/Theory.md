# Finding the Starting Point of Loop in LinkedList

- Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return null.
- There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
- Do not modify the linked list.

## Brute Force Approach 

### Algorithm

- [Watch it here](https://youtu.be/wiOo4DC5GGA?si=9EaDVTCsQauuDOgk&t=133)
- Take a temp at head 
- Use Hashmap to remember the nodes encountered (store the node in dict not just the data of the node)
- When you find the same node, return the node

### Code

```python 
# Node class represents a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data  
        self.next = next_node 

def detect_loop(head):
    node_map = {}
    temp = head

    while temp != None :
        if temp in node_map :
            return temp
        else :
            node_map[temp] = True
        temp = temp.next
    
    return None

if __name__ == "__main__":
    # Create a sample linked list with a loop
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node3 = Node(3)
    node2.next = node3
    node4 = Node(4)
    node3.next = node4
    node5 = Node(5)
    node4.next = node5

    # Make a loop from node5 to node2
    node5.next = node2

    # Set the head of the linked list
    head = node1

    # Detect the loop in the linked list
    loop_start_node = detect_loop(head)

    if loop_start_node:
        print("Loop detected. Starting node of the loop is:", loop_start_node.data)
    else:
        print("No loop detected in the linked list.")
```

- **Time Complexity : O(n * 2xlog(n)) or O(n * 2x1)** (depending on the map we use. In python, dict use O(1) time for searching and inserting)
- **Space Complexity : O(n)**

<br>

## Optimal Approach 

### Algorithm 

- [Watch it here](https://youtu.be/wiOo4DC5GGA?si=PLxf8n5gmiyTw9Zu&t=458)
- Use the Tortoise and Hare (slow and fast) poionter Algo
- When slow and fast collide, reset the fast pointer to the head again
- Move both the pointers now at the same 1 step now
- Where they collide again will be the starting point of the loop

<br>

### Code 

```python 
# Node class represents a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data  
        self.next = next_node 

def detect_loop(head):
    if head is None or head.next is None : return None

    slow = head
    fast = head 

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        # If collision, loop is detected
        if slow == fast : 
            fast = head

            # finding the start of the loop
            while slow != fast : 
                slow = slow.next
                fast = fast.next
            
            # next time the 2 will collide on the start of the loop
            return slow 
    
    return None
            

if __name__ == "__main__":
    # Create a sample linked list with a loop
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node3 = Node(3)
    node2.next = node3
    node4 = Node(4)
    node3.next = node4
    node5 = Node(5)
    node4.next = node5

    # Make a loop from node5 to node2
    node5.next = node2

    # Set the head of the linked list
    head = node1

    # Detect the loop in the linked list
    loop_start_node = detect_loop(head)

    if loop_start_node:
        print("Loop detected. Starting node of the loop is:", loop_start_node.data)
    else:
        print("No loop detected in the linked list.")
```

- **Time Complexity : O(n)**  (Somewhere around this, cannot pinpoint exactly)
- **Space Complexity : O(1)**