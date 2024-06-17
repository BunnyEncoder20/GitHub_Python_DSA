# Array Reverse

---

## Problem Statement
- **Given an array (or string), the task is to reverse the array/string.**

Examples:
```
 Input: original_array[] = {1, 2, 3} 
 Output: array_reversed[] = {3, 2, 1}

 Input: original_array[] = {4, 5, 1, 2}
 Output: array_reversed[] = {2, 1, 5, 4}
```

---

### Solution 1 - Array reversing using extra array (Non in-place)

-  Create a new array of the same size as the original array.
- Copy elements from the original array to the new array in reverse order.
- Code : 
```python 
def reverseArray(arr):
    return arr[::-1]    

if __name__ == '__main__':
    arr = [x for x in range(1,11)]
    revArr = reverseArray(arr)
    print("Array : ",arr)
    print("Reversed Array : ",revArr)
```
- Output : 
```
Array :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Reversed array :  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```
- Time Complexity : `O(n)`  (Linear time as we going over all the elements in the array)
- Space Complexity : `O(n)` (because new space for another array is needed)

---

### Solution 2 - Array reversing using a loop (In-place)

- Iterate through the array using two pointers (start and end).
- Swap elements at the start and end pointers.
- Move the start pointer towards the end and the end pointer towards the start until they meet or cross each other.
- **Code**
```python
def revArray(arr):
    start = 0
    end = len(arr)-1
    
    while start<end : 
        arr[start] , arr[end] = arr[end] , arr[start] # using this method to avoid making a new temp variable to swap the values
        start += 1
        end -= 1
        
    return arr 
        

if __name__ == '__main__':
    arr = [x for x in range(1,11)]
    print("Array: ", arr)
    revArray(arr)
    print("Reserved Array: ",arr)
```
- **NOTE** how in this approach we don't make a new array, just modify the original array.
- Output : 
```
Array:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Reserved Array:  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```
- Time Complexity : `O(n)`  (Linear time as we going over all the elements in the array)
- Space Complexity : `O(1)` (no additional space needed)

---

### Solution 3 - Array reversing using in-built methods (Non in-place)

- Use the in-built methods of python to reverse the array:
- **Code**
```python 
if __name__ == '__main__':
    arr = [x for x in range(1,11)]
    print("Array :",arr)
    arr.reverse()
    print("Reserved array: ",arr)
```
- Time Complexity : `O(n)` (cause this method also goes over all the elements)
- Space Complexity : `O(1)` (no new array created)

---

### Solution 4 - Array reversing using recursion (in-place or non in-place)
- Absolute trash method cause it is recursive 
- Time Complexity : `O(n)`
- Space Complexity : `O(n)`

--- 

### Solution 5 - Array reversing using Stack (Non in-place)

- Push each element of the array onto a stack.
- Pop elements from the stack to form the reversed array.
- **Code**
```python 
if __name__ == '__main__':
    arr = [x for x in range(1,11)]
    print("Array :",arr)
    stack = []
    for i in arr:
        stack.append(i)
    
    # NOTE this doesn't assign the element with the new value
    # for element in arr:
    #     element = stack.pop()
    # This is because element is just a temp variable. So changing element will not have any effect on the original array.
    
    # This is the proper way of assign new value in the list : 
    for i in range(0, len(arr)):
        arr[i] = stack.pop()
    
    print("Reserved array: ",arr)
```
- Output 
```
Array : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Reserved array:  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```
- Time Complexity : `O(n)`
- Space Complexity : `O(n)`