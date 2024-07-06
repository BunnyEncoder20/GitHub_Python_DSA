# Search Element in a Rotated Sorted Array

- Given an integer array arr of size `N`, sorted in ascending order (with distinct values) and a target value `k`. 
- Now the array is rotated at some pivot point unknown to you. Find the index at which `k` is present and if `k` is not present return -1.
- Examples 
```
Example 1:
Input Format: arr = [4,5,6,7,0,1,2,3], k = 0
Result: 4
Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.
```
```
Example 2:
Input Format: arr = [4,5,6,7,0,1,2], k = 3
Result: -1
Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.
```


<br>

## Brute Force Approach 

### Algorithm

- Linear search algorithm 

### Code 

```python 
def search(arr, n, target):
    for i in range(n):
        if arr[i]==target : return i 
    return -1
    
if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)
```
- Time complexity : O(n)
- Space complexity : O(1)

<br>

## Optimal Approach

- Whenever there is search and the search space is sorted, we need to apply Binary search

### Algorithm

1. We will use Binary Search to identify a mid 
2. Before we eliminate one of the halfs because the element doesn't lie in that range, we need to ensure that half of the array is sorted.
3. Hence we need to identify the sorted half first, then check for the element in that half.
4. If the element is not there, we can eliminate that half
5. Always one of the halfs will be sorted.

### Code 

```python 
def search(arr, n, target):
    low = 0
    high = n-1

    while low<=high:
        mid = (low+high)//2

        if arr[mid]==target: return mid

        # if left side is sorted : 
        if arr[low]<=arr[mid] : 
            if target in arr[low:mid+1]:
                high = mid-1
            else:
                low = mid+1
        
        # If  right side is  sorted
        else:
            if target in arr[mid:high+1]:
                low = mid+1
            else:
                high = mid-1
    
    # Dummy return cause answer is gauranteed 
    return -1
    
if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)
```
- Time complexity : O(log<sub>2</sub>N)
- Space complexity : O(1)

<br>

---
---