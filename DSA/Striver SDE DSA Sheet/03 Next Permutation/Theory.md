# Next Permutation

- Given a List of integers, find the next permutation of the List. 
- The numbers can be rearranged to generate various permutations (arrangements) of the numbers.
- Eg:
```
let given arr = [3,1,2]
All possible Permutations include:
[1,2,3], 
[1,3,2], 
[2,1,3], 
[2,3,1], 
[3,1,2], 
[3,2,1]
As given permutation is at index 4, we return the next index permutation i.e. [3,2,1]
```
---
## Printing all Permutations Recursively - Approach 1

- We gonna need a the number in a list, 2 data structures: stack(for keep track of current combination) and dictionary (to see which numbers we have already taken) and another list to store the resultant permutations.
- **Time complexity will be `O(N!xN)`**
- **Space complexity will be `O(N)+O(N)`**
- Below the Brute Force approach for the same: 

```python
def recursivePermutations(number, stack, mapping, answer):

    # Base case (ending case)
    if len(stack)==len(number):
        answer.append(stack[:]) # stack[:] reacts a deep copy of the stack, so that it doesn't reference the original stack ds 
        return
    
    # if the stack is not filled: (remaining cases)
    for i in range(len(number)):
        if not mapping[number[i]] :
            mapping[number[i]] = True
            stack.append(number[i])
            recursivePermutations(number, stack, mapping, answer)
            
            # After we come back from the recursion end, we remove the number from the ds and map
            stack.pop()
            mapping[number[i]] = False

if __name__ == '__main__':
    number = [3,2,1]
    stack = []
    mapping = {num:False for num in number}
    answer = []
    
    # number.sort()     # can do this to sort the permutations
    recursivePermutations(number,stack,mapping,answer)
    answer.sort()       # or can do this to sort the permutations
    print(answer)
```
- The above approach, the time complexity is `O(N!xN)` and the space complexity is `O(N)+O(N)`. The space complexity is not good and the below approach fixes this. 

---

## Printing all Permutations Recursively - Approach 2

- In this approach, instead of using a stack and dictionary which use extra memory, we swap the numbers within the original DS. 
- The numbers to the left of the index, are fixed and the numbers to the right of the index, are to be swapped. Then for the next recursion, the index is moved more towards the right
- This is done recursively until the index == len(number).
- This way, we do not use any extra space, which improves the space complexity to `O(1)`.

```python
def recursivePermutations(index, number, answer):
    
    # Ending case 
    if index == len(number):
        answer.append(number[:])
        return 
    
    # Other cases 
    for i range(index,len(number)):
        swap(index,i,number) # swap for new combination
        recursivePermutations(index+1, number, answer)
        swap(index,i,number) # un swap to get original number back


def swap(i, j, number):
    temp = number[i]
    number[i] = number[j]
    number[j] = temp

if __name__ == '__main__':
    number = [3,2,1]
    number.sort()
    index = 0
    answer = []
    recursivePermutations(index, number, answer)
    print(answer)
```

---
---
## Brute Force 

- Generate all the possible permutations in **sorted order** (using **recursion**: if the n is number of elements in the list, then the total possible permutations is **n!** )
- Find the position of the given permutation using Linear Search
- Return the next permutation of the List. (return first permutation if the given permutation is the last permutation in the list)
- **Time complexity: O(N!xN)**  (very bad time complexity)

<br>

- **NOTE:** never deep dive into a brute force solution in an interview. Should only explain it from a high level. 
- In Interview, people want to know the better and optimal solution only. 
- Explain the brute force solution in a shallow way and conclude by saying that this will take a Time complexity of very high order, hence I'll try to optimize it. 

---

## Better 

- A better solution would be use the inbuilt nextPermutation function available in the STL library of C++.
- However, other languages like Java, Python do have this inbuilt function. 

---

## Optimal

### Observations 

- Longer prefix match. (Just like adjacent words in a dictionary, the next word will be similar to the current number)
- If we lock all the digits and start rearrange the digits from the right side (starting with 2 digits, then 3, 4 and so on)
- We observe that the current unlocked digit should have a digit greater than itself in order to make a permutations greater than the given number. 

<br>

>1.  Hence we need to figure out this breakpoint to the left of which everything is smaller : `a[i] < a[i+1]`
>2. Find an digit which is just greator than that breakpoint digit. `a[x] > a[i] but closest to a[i]`
>3. Once the breakpoint element is made greater, now we can rearrange the remaining numbers in a sorted manner, to get the smallest number.

<br>

### Algorithm

1. First we must find the breakpoint from the right side where the left digit is smaller than the right one.
- Eg:
```python
[1,2,3,4,5]     # breakpoint is index n-2 (i.e: 4)
[2,1,5,4,3,0,0] # breakpoint is index 1 (i.e: 1)
[5,4,3,2,1]     # no breakpoint cause this is the largest permutation possible.
```
- For **example 2**, we just need to reverse the number to get the next (first) permutation.
- Algo for that can be summarized as:
```python
if (breakpoint == -1):
    number.reverse()
```

<br>

2. Once we have found the breakpoint element, we need to swap it with the rightmost digit which is just greater than it.
- For example 2, we see that breakpoint element is 1. (index = 1).
- We run a loop from the end of the number till we find a digit which is greater than the breakpoint element. We then swap these 2 digits. 

```python
n = len(number)
for i in range(n-1,breakpoint-1,-1):
    if(number[i]>num[breakpoint]):
        swap(number[i],number[breakpoint])
        break
```

<br>

3. Next we just need to reverse all the digits to the right of the swapped breakpoint now, to get the smallest permutation of that part of the number: 

```python
reverse(number, breakpoint, n-1)
```

<br>
<br>

### Code

- **Time Complexity :** `O(n)`
- **Space Complexity :** `O(1)` [in-place modification]
```python
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Step 1) Finding the breakpoint
        breakpoint = -1
        n = len(nums)
        
        for i in range(n-2,-1,-1):  
            if(nums[i]<nums[i+1]):
                breakpoint = i
                break
        
        if breakpoint == -1:
            nums.reverse()
            return
        
        
        # Step 2) Swapping breakpoint digit with one which is just greater than it on the right side
        for i in range(n-1,breakpoint,-1):
            if(nums[i]>nums[breakpoint]):
                nums[i],nums[breakpoint]=nums[breakpoint],nums[i]
                break   # don't forget this break
                
        # Step 3) reversing the digits on the right side of the breakpoint to get next permutation
        nums[breakpoint+1:] = reversed(nums[breakpoint+1:])
        


if __name__=="__main__":
    list_of_numbers = [[1,3,2]]
    classInstance = Solution()
    
    for num in list_of_numbers:
        num = classInstance.nextPermutation(num)
    
    for num in list_of_numbers:
        print(num)
```