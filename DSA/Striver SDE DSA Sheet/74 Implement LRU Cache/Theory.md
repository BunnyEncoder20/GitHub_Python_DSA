# Implement LRU Cache

- Design a data structure that follows the constraints of Least Recently Used (LRU) cache.
- Implement the LRUCache class:
    - LRUCache(int capacity) we need to initialize the LRU cache with positive size capacity.
    - int get(int key) returns the value of the key if the key exists, otherwise return -1.
    - Void put(int key,int value), Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
    - if the number of keys exceeds the capacity from this operation, evict the least recently used key.
- The functions get and put must each run in `O(1)` average time complexity.
- Exmaples : 
```
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

<br>

## Optimal Solution 

- We can brute force the solution using Arrays, but that would take O(n) Time complexity 
- We will use hashmap and Doubly LinkedList instead to get better complexity 

### Alogorithm 

- [Watch it here](https://youtu.be/xDEuM5qa0zg?si=pvFBwfaqJjuScER6&t=312)
1. Initial config of DLL will have a Head and a tail and a empty hashmap
2. For put instructions, we put the key:value pair right after head (Towards the head are the most recently used nodes) and add the key:address pair into the hashmap
3. For get operations, we check if the key is present in the hashmap, if it is , we just delete the node from the DLL and insert it again right after the head node (to maintain the order of LRU) and then return the value of the get(key)
4. If the value is not there in hashmap, return -1

### Code 

```python
<<<<<<< HEAD
class LRUCache:
    
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
    
    def __init__(self,size):
        self.size = size
        head = Node(-1,-1)
        tail = Node(-1,-1)

        head.next = tail
        tail.prev = head
        hashmap = {}
    
    def add_node(self, new_node):
        second_node = head.next
        new_node.next = second_node
        second_node.prev = new_node
        head.next = new_node
        new_node.prev = head
    
    def get(self,key):
        if key in hashmap:
            result_node = hashmap[key]
            result_value = result_node.value
            
            # del the key from the hashmap and remove the DLL node
            del hashmap[key]
            remove_node(result_node)
            
            # Add the node to the most recent used position and add it back into the hashmap
            add_node(result_node)
            hashmap[key] = head.next 
        else:
            return -1
    
    def put(self,key,value):
        if key in hashmap:
            existing_node = hashmap[key]
            del hashmap[key]
            remove_node(existing_node)
        if len(hashmap)==self.size:
            del hashmap[tail.prev.key]
            remove_node(tail.prev)
        
        # Inserting the new node 
        new_node = Node(key,value)
        add_node(new_Node)
        hashmap[key] = head.next
=======
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
>>>>>>> 3d1f7f9f2efb32fc41e5a13b0e29bb104a6e1898

class LRUCache:
    
    def __init__(self,size):
        self.size = size
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
    
    def add_node(self, new_node):
        second_node = self.head.next
        new_node.next = second_node
        second_node.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
    
    def remove_node(self,del_node):
        del_prev = del_node.prev
        del_next = del_node.next
        del_prev.next = del_next
        del_next.prev = del_prev 
    
    def get(self,key):
        if key in self.hashmap:
            result_node = self.hashmap[key]
            result_value = result_node.value
            
            # del the key from the hashmap and remove the DLL node
            del self.hashmap[key]
            self.remove_node(result_node)
            
            # Add the node to the most recent used position and add it back into the hashmap
            self.add_node(result_node)
            self.hashmap[key] = self.head.next 

            # Return the value 
            return result_value
        else:
            return -1
    
    def put(self,key,value):
        if key in self.hashmap:
            existing_node = self.hashmap[key]
            del self.hashmap[key]
            self.remove_node(existing_node)
        if len(self.hashmap)==self.size:
            del self.hashmap[self.tail.prev.key]
            self.remove_node(self.tail.prev)
        
        # Inserting the new node 
        new_node = Node(key,value)
        self.add_node(new_node)
        self.hashmap[key] = self.head.next

if __name__ == "__main__":
    l = LRUCache(2)
    print(l.put(1,1))
    print(l.put(2,2))
    print(l.get(1))
    print(l.put(3,3))
    print(l.get(2))
    print(l.put(4,4))
    print(l.get(1))
    print(l.get(3))
    print(l.get(4))
    # [null, null, 1, null, -1, null, -1, 3, 4]
```
- Time complexity : O(1)
<<<<<<< HEAD
- Space complexity : O(n)
=======
  - Using a unordered map will have a best and avg time complexity of O(1)
  - However in very very very rare cases (when collisions occur) it could take O(n) time
  - Hence we consider the TC to be O(1)
- Space complexity : O(n)
  - Where n is the size of the LRUCache 

<br>

---
---
>>>>>>> 3d1f7f9f2efb32fc41e5a13b0e29bb104a6e1898
