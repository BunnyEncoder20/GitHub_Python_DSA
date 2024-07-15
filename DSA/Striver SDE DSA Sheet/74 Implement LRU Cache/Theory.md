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

```
- Time complexity : 
- Space complexity : 