# Maximum Sub Array Problem 

--- 

## Problem Statement

**Given an integer array `nums`, find the subarray
with the largest sum, and return its sum.**

Example 1:

> Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
> Output: 6
> Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

> Input: nums = [1]
> Output: 1
> Explanation: The subarray [1] has the largest sum 1.

Example 3:

> Input: nums = [5,4,-1,7,8]
> Output: 23
> Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

- Constraints:

1. ` 1 <= nums.length <= 105`
2. `-104 <= nums[i] <= 104`

_Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle._

---

### Understanding the Problem 

- Subarray is
  - contiguous elements within the array
  - can be a single element as well
  - can be the entire array itself 
  - But the elements has to be contiguous 
- We need to find such a subArray or adjacent elements whose sum is the greatest 

---

## Solutions 

### 1. Brute Force

- Iterate through the array and find the subarray with the largest sum. 
- **Code**
```python 
def getMaxSubArray(nums):
    
    if(len(nums)==1):
        return nums,nums[0]
    
    maxSum = nums[0]+nums[1]
    maxSubArray = []
    
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if sum(nums[i:j+1]) > maxSum :
                maxSum = sum(nums[i:j+1])
                maxSubArray = nums[i:j+1]
    
    return maxSubArray,maxSum

if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    maxSubArray, maxSum = getMaxSubArray(nums)
    print(f"The subarray {maxSubArray} has the largest sum {maxSum}.")
```
- Time Complexity: `O(n^3)`   
  - because of double loop and loop for the sum() method
- Space Complexity: `O(n)`    
  - because of maxSubArray

---

### 2. Kadane's Algorithm 

>- Go through each index and add the element to the sum.
>- If at any moment, the sum is negative, reinitialize sum to zero (only carry sum forward, if the value of it is positive)
>- Compare the sum value with the maxSum and if it is more, update the maxSum value 
  
<br>

- Time complexity : **`O(n)`**
- Space complexity : **`O(1)`** (if you do not store the subarray, else `O(n)`)
<br>

- **Code**
```python 
def getMaxSubArray(nums):
    
    if(len(nums)==1):
        return nums,nums[0]
    
    maxSum = float('-inf')
    start,summation=0,0
    maxSubArray = []
    
    for i in range(len(nums)):
        summation += nums[i]
        
        if summation > maxSum:
            maxSum = summation
            maxSubArray = nums[start:i+1]
        
        if summation < 0:
            summation = 0
            start = i+1
    
    return maxSubArray,maxSum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [5,4,-1,7,8]
    maxSubArray, maxSum = getMaxSubArray(nums)
    print(f"The subarray {maxSubArray} has the largest sum {maxSum}.")
```