# Sorting an Array of 0, 1 and 2

- Seems easy but it's optimal solution is not so easy 

## Brute Force

- Using any sorting algorithm sort the array.
- For example, let us consider merge sort.
- **Time Complexity : O(NlogN)**
- **Space Complexity : O(N)** [temp array used in merge sort]

### Merge Sort (Divide and Merge)

- We start with a arr of numbers 
- We recursively divide the array into 2 parts till we have only 1 element left 
- Now we have to merge the single elements while coming back up, but in a sorted manner.

#### Pseudo Code

- Instead of making new arrays each time, we use variables to store the indexes. 
    - low (for the starting index)
    - high (for the end index)
- Find below the pseudo code for the divide algorithm:
```python
mergeSort(arr, low, high):

    if low == high: return

    mid = (low+high)//2

    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)

    merge(arr, low, mid, high)
```
- Below is the pseudo code for the merge algorithm 
```python
merge(arr, low, mid, high):
    left = low
    right = mid+1
    temp = []

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else :
            temp.append(arr[right])
            right+=1

    # adding the remaining elements when one side array finishes
    while left <= mid:
        temp.append(arr[left])
        left+=1
    while right <= high:
        temp.append(arr[right])
        right+=1

    # copying the temp array into the original array
    for i in range(low, high+1):
        arr[i] = temp[i-low]
```

<br>

- Below is the code implementation of merge sort:

```python 
def mergeSort(arr, low, high):
    if low >= high: return
    
    mid = (low+high)//2
    
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    
    merge(arr, low, mid, high)
    

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1
    
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    while left<= mid:
        temp.append(arr[left])
        left+=1
    while right<= high:
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i] = temp[i-low]

if __name__ == '__main__':
    nums = [1,3,2,5,6,1,7,9,8]
    mergeSort(nums,0,len(nums)-1)
    print(nums)
```

---

## Better 

- take 3 counter variables : 
  - count0
  - count1
  - count2
- Loop through the array once and update the count0, count1 and count2 accordingly.
- Finally loop through the array and update the array with 0's count0 times, 1's count1 times and 2's count2 times.
- **Time Complexity : O(2N)**
- **Space Complexity : O(1)**

```python

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0,count1,count2 = 0,0,0
        
        for num in nums:
            if num == 0:
                count0+=1
            elif num == 1:
                count1+=1
            else :
                count2+=1
        
        for i in range(count0):
            nums[i] = 0
        for j in range(count0,count0+count1):
            nums[j] = 1
        for k in range(count0+count1,count0+count1+count2):
            nums[k] = 2

if __name__=='__main__':
    nums1,nums2 = [2,0,2,1,1,0] , [2,0,1]
    sol = Solution()
    sol.sortColors(nums1)
    sol.sortColors(nums2)
    print(nums1)
    print(nums2)
```

---

## Optimal (Dutch National flag Algorithm)

- The Algorithm will use 3 poiunters :
  - low
  - mid
  - high
- The Algorithm is revolving around 3 rules :
1. Everything between [0 : low-1] will be 0 (extreme left)
2. Everything from [low : mid-1]  will be 1
3. Everything from [high+1 : n-1] will be 2 (extreme right)

<br>

- The above rules divide the arr into 4 sections :
    1. [0 : low-1] : which keeps all the 0
    2. [low : mid-1] : which keeps all the 1
    3. [mid : high] : which keeps 0,1,2 in unsorted manner
    4. [high+1 : n-1] : which keeps all the 2

### Algorithm 
- We start by making the points
    - mid = 0 , high = n-1 (the unsorted region)
    - low = 0
- In our algo, we'll be solving wrt a[mid]
- a[mid] can have any of these 3 cases :
    - a[mid] = 0 :
        - swap(a[low] , a[mid]) ;
        - low+=1 ; mid+=1 ;
    - a[mid] = 1 :
        - mid+=1
    - a[mid] = 2 :
        - swap(a[mid] , a[high]) ;
        - high-=1;
- We repeat this process untill mid > high
