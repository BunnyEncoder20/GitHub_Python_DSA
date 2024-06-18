# Detect Cycle in LinkedList

- Given head, the `head` of a linked list, determine if the linked list has a `cycle` in it.
- There is a `cycle` in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
- Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

<br>

## Brute Force Approach

- Using Hashing, remember the nodes which were visited.

### Algorithm 

- [Watch it here](https://youtu.be/wiOo4DC5GGA?si=sJ2UB9bmy0zC4V-k&t=132)
- Traverse the LL and store the nodes in the hashmap
- If a node in present already in the hashmap, return True else return False

### Code

```python 
def detect_loop(head):
    node_map = {}
    pointer = head
    while pointer != None:
        if pointer in node_map: 
            return True
        else:
            node_map[pointer] = True
    return False
```
- **Time complexity : O(n + 2xlog(n)) or O(n + 2x1)** (if the map takes O(1) time)
- **Space complexity : O(n)**

<br>

## Optimal Approach

- Using the **Tortoise and Hare algorithm**. 
- Optimized the Space complexity by not using eternal DS

### Algorithm

- [Watch it here](https://youtu.be/wiOo4DC5GGA?si=F3gcMoEeS9rDypkq&t=475)
- Slow pointer moves 1 step at a time
- Fast pointer moves 2 step at a time
- If they meet , return True cause there was a loop
- Else if fast.next == None : return False

## Code 

```python
def detect_loop(head):
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast : return True 
    
    return False
```
- **Time complexity : O(n)**    (not fixed, depends on the input)
- **Space complexity : O(1)**