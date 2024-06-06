# Inversion of an Array (Count Inversion)

- Pre-requisite : Merge Sort 
- You will be given a array of integers and we have to return pairs such that :
  - i < j 
  - a[i] > a[j]
- Eg:
```
Sample Input 1 :
3
3 2 1

Sample Output 1 :
3

Explanation of Sample Output 1:
We have a total of 3 pairs which satisfy the condition of inversion: 
(3, 2), (2, 1) and (3, 1).

Sample Input 2 :

5
2 5 1 3 4

Sample Output 2 :

4

Explanation of Sample Output 1:

We have a total of 4 pairs which satisfy the condition of inversion. 
(2, 1), (5, 1), (5, 3) and (5, 4).
```

---

## Brute Force Solution

- **Time Complexity: O(n<sup>2</sup>)**
- **Space Complexity: O(1)**

### Algorithm 

1. Make a pointer at the first element of the array
2. Make another pointer traverse the elements to the right of that first pointer 
3. We count the number of inverse pairs 

### Code 

```python 
def getInversions(arr,n):
    counter = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j] : counter+=1
    
    return counter
```

--- 

## Optimal Solution

- We use the merge sort method to look for the inversion pairs 
- At the bottom, at each step, there will be 2 arrays (that are going to be merged) which are sorted.
- The left array elements will look at the right array to for pairs. 
- If the left side element is greater than the right side element, we have an inversion pair.
- But we'll add counter + (no. of elements to the right of element) as all of them will be greater than that
- That i.e; counter += (mid-left+1)
- As soon as the right side elements are over, we merge the arrays for the next iteration of merge sort and repeat the process.

### Code

```python 
def getInversions(arr,n):
    return mergeSort(arr,0,len(arr)-1)


def mergeSort(arr,low,high):
    count = 0                       # mod 1
    
    if low>=high : return count     # mod 2
    
    mid = (low+high)//2
    
    count += mergeSort(arr,low,mid)     # mod 3
    count += mergeSort(arr,mid+1,high)  # mod 4
    
    count += merge(arr,low,mid,high)    # mod 5
    
    return count                        # mod 6


def merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []
    count = 0                           # mod 7
    
    while left<=mid and right<=high :
        if arr[left] <= arr[right] : 
            temp.append(arr[left])
            left+=1
        else :
            temp.append(arr[right])
            right+=1
            count += (mid-left+1)      # mod 8
        
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    
    for i in range(low,high+1):
            arr[i] = temp[i-low]
        
    return count                # mod 9
```