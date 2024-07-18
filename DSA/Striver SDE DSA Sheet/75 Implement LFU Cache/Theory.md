# Implement LFU Cache 

- Implement the function of LFU (least frequently used) Cache. 
- The LFU cache has the following functionality:
  - get(key) : if the key exists in the cache returns the value of it else -1.
  - put(key,value) : insert the key:value into the cache, if already there, update the value of the key. 
  - If the cache is already full, remove the least frequency used pair and insert the new one.
  - If there are multiple pairs which have same value of least frequency, then eleminate the one which is least recently used among them.
- Both the functions msut be executed in O(1)
- Exmaples : 
```
Example 1 

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key 
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
```

<br>

## The Only Optimal Solution (No time for brute force appproach)

- We do not have time for brute force if this question comes cause the optimal solution itself is very long 

### Algorithm

- [Watch it here](https://youtu.be/0PSB9y8ehbk?si=P-p1rBzf4GLteI3o&t=500)
1. We will require the following DS:
   1. `hashmap<freq:int , list:DLL>` : Our frequency map which holds the frequency as key and a DLL of all the nodes which have that frequency
   2. `hashmap<key:int, node:Node>` : key map which holds the addresses of the nodes
2. We will require the following variables:
   1. `LF` = for keeping track of the least frequency
   2. `capacity` = for keeping track of the size of the cache
3. When we inserting into the cache check the following:
   1. Is the key already there in the key map
   2. Is there space in the cache b checking the capacity 
4. Create a key of the current freqency and make a doubly linked list for it's value. Insert the key:value pair as a node into the DLL. **(Ensure that this DLL follows the rules of LRU cache)**
5. Update the LF if required and the capacity and the key map.
6. If the cache is full, do to the LF key in frequency map and remove the LRU pair. Then insert the new pair at the correct frequency point with a new DLL ir necessary.
7. When getting the nodes, don't forget to remove the nodes from their old frequency keys and move them up to the higher frequency key.
8. If the DLL for a frequency becomes empty, update the LF variable. Will also be updated if a new node comes which previously didn't existed (LF can also decrease)

### Code 

```python
from turtle import update


class Node:
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.freq = 0

class LRUCache:
    def __init__(self) -> None:
        self.size = 0
        self.keymap = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self,new_node):
        second_node = self.head.next 
        self.head.next = new_node
        new_node.next = second_node
        second_node.prev = new_node
        new_node.prev = self.head
        self.size+=1

    def remove_node(self,del_node):
        del_node_prev = del_node.prev
        del_node_next = del_node.next
        del_node_prev.next = del_node_next
        del_node_next.prev = del_node_prev
        self.size-=1


class LFUCache:
    def __init__(self,limit) -> None:
        self.freqmap = {}
        self.keymap = {}
        self.maxCacheLimit = limit
        self.LF = 1
        self.size = 0
    
    def get(self,key):
        if key in self.keymap:
            node = self.keymap[key]
            node_val = node.value

            # increase the frequency
            self.update_freq(node)

            return node_val
        else:
            return -1
        
    def update_freq(self,node):
        current_freq = node.freq

        if current_freq in self.freqmap : 
            old_dll = self.freqmap[current_freq]
            old_dll.remove_node(node)
            del self.keymap[node.key]

            if current_freq == self.LF and old_dll.size==0:
                self.LF += 1
        
        node.freq += 1

        if node.freq not in self.freqmap:
            self.freqmap[node.freq] = LRUCache()
        
        new_dll = self.freqmap[node.freq]
        new_dll.add_node(node)
        self.keymap[node.key] = node
    
    def put(self,key,val):
        if key in self.keymap:
            node = self.keymap[key]
            node.value = val
            self.update_freq(node)
            return

        if len(self.keymap)==self.maxCacheLimit:
            LFU_dll = self.freqmap[self.LF]
            LRU_node = LFU_dll.tail.prev
            LFU_dll.remove_node(LRU_node)
            del self.keymap[LRU_node.key]
        
        new_node = Node(key,val)
        self.keymap[key] = new_node
        self.update_freq(new_node)

if __name__ == "__main__":
    cache = LFUCache(2)
    print(cache.put(1,1))   # None
    print(cache.put(2,2))   # None
    print(cache.get(1))     # 1
    print(cache.put(3,3))   # None
    print(cache.get(2))     # -1
    print(cache.get(3))     # 3
    print(cache.put(4,4))   # None
    print(cache.get(1))     # -1 
    print(cache.get(3))     # 3 
    print(cache.get(4))     # 4

```
- Time complexity : O(1)
- Space complexity : O(n)
  - Where n is the capacity of the cache

<br>

---
---