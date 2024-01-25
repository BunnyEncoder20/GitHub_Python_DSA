# Arrays in DSA
---
Visualizing how the data of a array is stored in memory: 
![Image](./Notes%20Assets/arrayStorage.png)
- The actual data is stored in binary (bits) in the actual memory.
- The Lookup in a array is of the order `O(1)` (constant time operation) 
![Image](./Notes%20Assets/arrayLookUp.png)

- However when we are searching by a specific value, we increase the lookup time cause now we will have to compare each element of the array: 
![Image](./Notes%20Assets/arrayLookup2.png)
- A scenario for normal traversal will also have the same time complexity as `O(n)`
- If we want to **insert** a value into the array (in python list) we use the `.insert(element,position)` method (which takes 2 arguments, the element and the position where to insert it in) the time complexity us still `O(n)` because after adding the element, the function has to push all the elements one place to the next (to make space for the new element)
- Similarly when we want to **delete** an element, we use the `.remove(element)`.The function has to again remap all the remaining elements back up (to cover up the space left by deleted element), hence this too has a time complexity of `O(n)`
- **NOTE** that all the arrays we are talking about in python are actually lists. Lists in python are implemented as dynamic arrays. (C++ or Java has both static (default) and dynamic arrays)
- When dynamic arrays grow in size, they get additional overhead cause all the elements need to be shifted to a new memory location which has twice the memory spaces are the current memory block. Hence creating the new memory space and copying all the elements to the new location brings additional overhead times when ever the dynamic array grows in size.
- This is shown here  :
![Image](./Notes%20Assets/Lists%20increasing%20in%20size.png)

Hence to Summarize : 
![Image](./Notes%20Assets/Summary.png)
