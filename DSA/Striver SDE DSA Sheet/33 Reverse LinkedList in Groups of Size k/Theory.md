# Reverse Linked List in Groups of Size k

- Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.
- `k` is a positive integer and is less than or equal to the length of the linked list. 
- If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.
- You may not alter the values in the list's nodes, only nodes themselves may be changed.

<br>

## Approach 

### Algorithm 

- [Watch it here](https://youtu.be/lIar1skcQYI?si=f8yB9dDrmb4GePMU&t=132)
- Get the kth node of the group
- Separate the group from the rest of the LL
- reverse the group.
- Connect the prev group to this group
- Update the prev_group_node, next_group_node and temp/current pointers

### Code 

```python 
# Actual Problem Code
def kReverse(head,k):
    if k<1 or head is None: return head
    
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

        # separating the current group from the remaining LL
        kth_node.next = None

        ## reversing the group LL
        reversed_group_head = reverseLL(temp)

        # if it is the first group, reassign the new head 
        # else join the current group to the prev group
        if temp == head : 
            head = reversed_group_head
        else :
            prev_group_node.next = reversed_group_head 
        
        prev_group_node = temp
        temp = next_group_node
    
    return head
```
- Time complexity : O(2n) (finding Kth node and reversing the group)
- Space complexity : O(1)
