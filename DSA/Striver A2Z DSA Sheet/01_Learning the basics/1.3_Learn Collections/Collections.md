# Collections in Python

---

- Container Data types [Documentations](https://docs.python.org/3/library/collections.html)
- This module implements specialized container data types providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
- Most used is DEque (Doubly Ended Queue, pronounced as _decks_)

## DEque Object 

> class collections.deque([iterable], maxlen=optional)

- Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not specified, the new deque is empty.
-  Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
-  `maxlen` is used to fix the maximum size of the deque.
-  If not specified, the deque is unbound.
-  If specified, any new element append will remove the first inserted element of the deque and any subsequent insertions will remove the first entered elements (behaving in FIFO method)

<br>

## DEque Methods

|        **Method Name**        	|                                                                  **Description**                                                                  	|
|:-----------------------------:	|:-------------------------------------------------------------------------------------------------------------------------------------------------:	|
|         **append(x)**         	| Add x to the right side of the deque.                                                                                                             	|
|       **appendleft(x)**       	| Add x to the left side of the deque.                                                                                                              	|
|          **clear()**          	| Remove all elements from the deque leaving it with length 0.                                                                                      	|
|           **copy()**          	| Create a shallow copy of the deque.                                                                                                               	|
|          **count(x)**         	| Count the number of deque elements equal to x                                                                                                     	|
|      **extend(iterable)**     	| Extend the right side of the deque by appending elements from the iterable argument                                                               	|
|    **extendleft(iterable)**   	| Extend the left side of the deque by appending elements from iterable.                                                                            	|
| **index(x[, start[, stop]])** 	| Return the position of x in the deque (at or after index start and before index stop). Returns the first match or raises ValueError if not found. 	|
|        **insert(i, x)**       	| Insert x into the deque at position i. If insert causes bounded deque to grow in size, it'll raise a IndexError                                   	|
|           **pop()**           	| Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.                                  	|
|         **popleft()**         	| Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.                                   	|
|       **remove(value)**       	| Remove the first occurrence of value. If not found, raises a ValueError.                                                                          	|
|         **reverse()**         	| Reverse the elements of the deque in-place and then return None.                                                                                  	|
|        **rotate(n=1)**        	| Rotate the deque n steps to the right. If n is negative, rotate to the left.                                                                      	|

<br>

## 