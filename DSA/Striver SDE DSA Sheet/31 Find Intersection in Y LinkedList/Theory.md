# Find Intersection in Y LinkedList

- **Problem Statement:** Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. 
- If the two linked lists have no intersection at all, return `null`.

![alt text](image.png)

<br>

## Brute Force Approach 

- [Watch it here](https://youtu.be/u4FWXfgS8jw?si=1stvn0YLODv7Tf1q&t=86)

### Algorithm 

- Go node by node and check if the **nodes** are same (not their value)

### Code 

```python 
class Solution:
    def intersectionPresent(self, headA: Node, headB: Node) -> Optional[Node]:
        p1 = headA

        while p1 != None:
            p2 = headB
            while p2 != None:
                if p1 == p2 :
                    return p2
                p2 = p2.next
            p1 = p1.next
            
        return None
```
- **Time complexity : O(nxm)**
- **Space complexity : O(1)**

<br>

## Better Approach

- Can optimize the approach by using the hashing 

### Algorithm

1. [Watch it here](https://youtu.be/u4FWXfgS8jw?si=bF3B0HBuRfUrRe_W&t=187)
2. Traverse and hash all the nodes addresses in L1 and L2
3. If you encounter a node which is already in Hashtable, then return that node else none.

### Code 

```python
def intersectionPresent(head1,head2):
    hash_table = set()

    while head1:
        hash_table.add(head1)
        head1 = head1.next
    while head2:
        if head2 in hash_table:
            return head2
        head2 = head2.next
    
    return None
```
- **Time complexity : O(n+m)**
- **Space complexity : O(n)**   (cause of hash table)

<br>

## Optimal Approach 

### Algorithm 

- [Watch it here](https://youtu.be/u4FWXfgS8jw?si=7vbgTmqzJT-04yc0&t=733)
- Make 2 dummy nodes and iterate throughout the LinkedList.
- When a dummy node reaches it's LL end, we make it start over again but at other linkedlist. 
- hence the dummy nodes will cross over and they will be at same level once both have started over
- They will meet on the intersection node 

### Code 

```python 
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
```
- **Time complexity : O(2*max(len(l1),len(l2)))**
- **Space complexity : O(1)**