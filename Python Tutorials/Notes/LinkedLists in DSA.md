# LinkedLists in DSA (Python)
---
- There were some **issues** with traditional arrays, major one being their need to be in a **sequential block of memory**. 
- Hence when we want to **add** or **remove** an element from teh array, we get a complexity of `O(n)` because all the elements of the array need to be shifted
- also when using **dynamic array**, when the _pre-allocated_ space of memory is filled, the function will assign a new memory block with twice the space as previous **AND** copy all the elements to the new block. This causes `additional overhead`.
![Image](./Notes%20Assets/dynamicarrayallocation.png)

---

- LinkedList store elements in non sequential memory blocks. Each block has a pointer pointing to the next elements memory location. Looks something like this : 
![Image](./Notes%20Assets/llmemoryblock.png)