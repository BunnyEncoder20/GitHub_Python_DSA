# Next Greater Element Using Stack

- Given a circular integer array `A`, return the next greater element for every element in `A`. 
- The next greater element for an element `x` is the first element greater than `x` that we come across while traversing the array in a clockwise manner. 
- If it doesn't exist, return `-1` for this element.
- Examples
```
Example 1: 

Input: N = 11, A[] = {3,10,4,2,1,2,6,1,7,2,9}
Output: 10,-1,6,6,2,6,7,7,9,9,10
Explanation: For the first element in A ,i.e, 3, the greater element which comes next to it while traversing and is closest to it is 10.
Hence,10 is present on index 0 in the resultant array. 
Now for the second element,i.e, 10, there is no greater number and hence -1 is i
```
```
Example 2:

Input:  N = 6, A[] = {5,7,1,7,6,0}
Output: 7,-1,7,-1,7,5
```

<br>

## Brute Force Approach 

- [Watch it here](https://youtu.be/Du881K7Jtk8?si=S619l_uPx331ZHBz&t=172)
1. For every element, we look on the right side for a greater element
1. Once we encounter the next greatest element, we break off.

### Code 

```python
from typing import List
class Solution:
    def nextGreaterElements(self,arr:List[int]) -> List[int]:
        n = len(arr)
        nge = [-1]*n
        
        for i in range(n):
            for j in range(1,n):
                next_index = (i+j)%n
                if arr[i]<arr[next_index]:
                    nge[i] = arr[next_index]
                    break
        return nge

if __name__ == '__main__':
    obj = Solution()
    v = [5, 7, 1, 2, 6, 0]
    res = obj.nextGreaterElements(v)
    print("The next greater elements are")
    print(*res)
```
- **Time complexity : O(n<sup>2</sup>)**
- **Space complexity : O(n)**

<br>

## Optimal Solution 

- we can use the Stack DS for it's LIFO property

### Algorithm 

- [Watch it here](https://youtu.be/Du881K7Jtk8?si=lzwICoPfZPImadj1&t=345)
1. We use the stack and move from the last index of the array
2. If the stack top is not < current_element and stack is empty : nge[current] = -1 and push current_element into the stack 
3. If top is > then current_element, nge[current] = stack top
4. If the top < current_element then keep popping elements till the top of the stack is > current_element. Push the top once it is greater than current element and nge[current] = stack top
5. If while popping, stack becomes empty, nge[current] = -1

### Code

```python 
from typing import List 

class Solution:
    def nextGreaterElements(self,arr:List[int]) -> List[int]:
        n = len(arr)
        stack = []
        nge = [-1]*n
        for i in range(2*n-1,-1,-1):
            index = i%n
            
            # remove all the elements which were lower than the current element
            while stack and stack[-1] <= arr[index]:
                stack.pop()
            
            # Assign the top to the nge array
            if i<n : 
                if stack:
                    nge[i] = stack[-1]
            
            # push the element into the stack
            stack.append(arr[index])

        return nge
            
if __name__ == '__main__':
    obj = Solution()
    v = [5, 7, 1, 2, 6, 0]
    res = obj.nextGreaterElements(v)
    print("The next greater elements are")
    print(*res)
```
- **Time complexity : O(2n) + O(2n) = O(n)**
  - first O(2n) is outer for loop
  - second O(2n) is for the inner while loop. This is cause the inner while loop will run for a total of 2n time only (hence doesn't make it to quadratic time)
  - approax time complexity can be O(n)
- **Space complexity : O(n)**
  - for the stack used 

<br>

---
---