# LinkedLists in DSA (Python)
---
- There were some **issues** with traditional arrays, major one being their need to be in a **sequential block of memory**. 
- Hence when we want to **add** or **remove** an element from teh array, we get a complexity of `O(n)` because all the elements of the array need to be shifted
- also when using **dynamic array**, when the _pre-allocated_ space of memory is filled, the function will assign a new memory block with twice the space as previous **AND** copy all the elements to the new block. This causes `additional overhead`.
![Image](./Notes%20Assets/dynamicarrayallocation.png)

---

- LinkedList store elements in non sequential memory blocks. Each block has a pointer pointing to the next elements memory location. Looks something like this : 
![Image](./Notes%20Assets/llmemoryblock.png)
- Using these pointers or Links we can access the next element in the list. Also it is easier to add or remove an element , as we just have to change the links and do not need to always copy all the elements to new locations when the linkedlist grows in size. 
![Image](./Notes%20Assets/insertinginll.png)
- Insert/Delete Element **at beginning** = `0(1)`
- Insert/ Delete Element **at the end** = `O(n)`
- Traversing the LinkedList = `O(n)`
- Accessing element by value = `O(n)`
  
**Linked Lists** have 2 main benefits : 
1. Don't have to **pre-allocate** memory space
2. Insertion is easier
- LinkedList can be doubly linked also, called a **Doubly LinkedList** (pointer to both next and previous element)

###LinkedList VS Arrays
![Image](./Notes%20Assets/llvsarr.png)
- The one advantage array has over linkedlist is when we know the index of teh element we want. Then in array it is a constant time complexity of `O(1)`. Whereas in LinkedList it will be of `O(n)`
- Cause in LinkedList even if we know we want to access only the 5th element, we have to go though all the previous elements as well.
- Inserting/Deleting in arrays has addition 'amortized' cost due to expansion of the memory spaces when previous pre-allocated space runs out  

#### Implementing LinkedList in Python
```
class Node : 
    
```