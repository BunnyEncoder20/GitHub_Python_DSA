# Reverse Pairs 

- Given an integer array nums, return the number of reverse pairs in the array.
- A reverse pair is a pair (i, j) where:
    - 0 <= i < j < nums.length 
    - nums[i] > 2 * nums[j].
- Basically left element of pair should be greater than twice the right element.
- Eg:

```
Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
```

<br>

## Brute Force Approach 

- We take 2 pointers and iterate over the array
- Increment the counter when we get a pair 
- **Time Complexity : O(n<sup>2</sup>)**
- **Space Complexity : O(1)**
  
### Algorithm : 

1. First pointer for the first loop
2. Second pointer for the second loop
3. if first[i] > 2*second[j] increment the counter
4. Return counter.

<br>

### Code 

```python 
def reversePairs(nums: List[int]) -> int:
    counter = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] > 2*nums[j] : counter+=1
    
    return counter
```

---

## Optimal Approach 

- Think of a different problem where in, you are given 2 sorted arrays: left and right.
- We need to make pairs such that left_element > 2*right_element

<br>

- To solve the above different problem, we know that if the pointer is a left_element which is greater than 2xright_element, then all the elements on the left array after that element will also be greater than that 2xright_element.
- Also if a left_element forms a pair with some right_elements. Then We can be sure that those righht_elements will also forma a pair with the next left_element.
- Thus we don't need to count all the right elements, we can just assume that the current left_element will form a pair with all the previous right_elements of the right pointer.

<br>

Hence we can solve our original problem in a similar way to count inverse's optimal approach which leveraged merge sort algorithm.

### Algorithm 

1. Apply merge sort algorithm on the array
2. Before starting to merge, we check for the Reverse pairs.
3. left pointer iterates over the left side, checks if the right pointer element forms a pair.
4. If it does, we add right_pointer elements (index=no. of elements before our current index) to the counter. and move the right_pointer by one.
5. if the left_pointer completes the iteration, we return the counter.
6. We merge the array and return the counter.

<br>

### Code 

```python
from typing import List 

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        low = 0
        high = len(nums)-1
        
        self.mergeSort(nums,low,high)
        return self.count
    
    def mergeSort(self,arr,low,high):
        # count = 0
        if low>=high : return 
        
        mid = (low+high)//2
        
        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.countPairs(arr,low,mid,high)
        
        self.merge(arr,low,mid,high)
    
    def countPairs(self,arr,low,mid,high):
        right = mid+1
        left = low
        while left <= mid :
            while right<=high and arr[left]>2*arr[right]:
                right+=1
            self.count += (right-(mid+1))
            left+=1
    
    def merge(self, arr, low, mid, high):
        left = low
        right = mid+1
        temp = []
        
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        
        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right+=1
        
        for i in range(low,high+1):
            arr[i] = temp[i-low]
            
        
        
    
if __name__ == "__main__":
    i = Solution()
    listNums = [[1,3,2,3,1],[2,4,3,5,1]]
    for nums in listNums : 
        print(i.reversePairs(nums))
```