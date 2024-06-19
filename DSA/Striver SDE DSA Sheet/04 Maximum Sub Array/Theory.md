# Maximum Sub Array (Kadane's Algorithm)

- Sub array is contiguous (continuous) part of an array. 
- The entire array itself and just a single element are also sub array.
- We need to return the maximum sum we can get from a sub array of the given array.

<br>

## Brute

- Trying out all the possible sub arrays of the given array.
- Whichever of those gives the largest sum will be returned.
- Given Below is code for the same:

```python
def maxSubArrays(arr):
    n = len(arr)
    maxi = float('-inf')
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
            maxi = max(maxi,sum)
    return maxi

if __name__ == '__main__':
    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    print(maxSubArrays(arr))        # 7
```
- **Time Complexity** = **O(n<sup>3</sup>)**
- **Space Complexity** = **O(1)**

---

## Better 

- Instead of keeping the sum variable inside the 2nd loop, we keep it in the first loop and keep adding the sum to it.
- **Time Complexity : O(n<sup>2</sup>)**
- **Space Complexity : O(1)**

---

## Optimal (Kadane's Algorithm)

- Instead of checking each and every sum, we can use the concept of Kadane's Algorithm.
- We initialize 2 variables :
  - `maxSum` which will keep track of the maximum sum we have found so far.
  - `currSum` which will keep track of the sum of the current sub array we are on.
- If the currSum value is negative, we will reset it to 0.
- If the currSum is greater than maxSum, we will update the maxSum value.

<br>

- The algorithm is coded below : 
  
```python
def maximum_subArray(nums):
    maxSum = float('-inf')
    currSum = 0
    
    for i in range(0, len(nums)):
        currSum += nums[i]

        maxSum = max(maxSum, currSum)
        
        if currSum < 0:
            currSum = 0
    
    return maxSum if maxSum > 0 else 0

if __name__ == '__main__':
    nums = [-2, -5, 6, -2, -3, 1, 5, -6]
    print(maximum_subArray(nums))
```

### Follow up Question : Also print the sub array

- we can also print the sub array section with the maximum sum by slightly modifying the above code:

```python 
def maximum_subArray(nums):
    maxSum = float('-inf')
    currSum = 0
    start,end = 0,0
    
    
    for i in range(0, len(nums)):
        if currSum == 0:
            start = i
        
        currSum += nums[i]

        if maxSum < currSum:
            maxSum = currSum
            end = i
        
        if currSum < 0:
            currSum = 0
    
    print("MaxSum : ", maxSum)
    print("MaxSubArray : ", nums[start:end+1])
```

---