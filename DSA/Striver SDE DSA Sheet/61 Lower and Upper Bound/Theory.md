# Implementing Lower and Upper Bound 

## Lower Bound

- Lower Bound = smallest index such that `arr[i] >= n`
- We could do a linear search but that is inefficient here
- As the array is already sorted, we can implement Binary Search here

### Algorithm 

1. Keep a hypothetical answer = len(arr) (**This is a important trick for BS**)
2. find mid. If it satisfies the condition arr[i]>=n : it might be our answer , so we store in the ans variable
3. Keep repeating till low<=high

### Code 

```python
def lowerBound(arr,target,n):
    low = 0
    high = n-1
    ans = n
    
    while low<=high:
        mid = (low+high)//2     # there are only 2 possibilities : 
        
        if arr[mid]>=target:    # this might be an answer 
            ans = mid
            high = mid-1
        else :                  # or not the answer
            low = mid+1
            
    return ans

if __name__ == "__main__":
    arr = [1,2,3,3,5,8,8,10,10,11]
    n = len(arr)
    targets = [1,9]
    
    for target in targets:
        print("The lower bound is : ",lowerBound(arr,target,n))
         
```
- **Time complexity : O(log<sub>2</sub>N)**
- **Space complexity : O(1)**

<br>

## Upper Bound

- The smallest index such that `arr[i] > target` (lower was >=)
- It is the same concept as lower bound

### Algorithm 

1. Keep a hypothetical answer = len(arr) (**This is a important trick for BS**)
2. find mid. If it satisfies the condition `arr[i]>n` : it might be our answer , so we store in the ans variable
3. Keep repeating till low<=high 
4. If no ans is found, we will return our hypothetical answer

### Code

```python
def upperBound(arr,target,n):
    low = 0 
    high = n-1
    ans = n
    
    while low<=high:
        mid = (low+high)//2         # There are again only 2 possibilities here

        if target<arr[mid] :        
            ans = mid               # this might be the answer 
            high = mid-1
        else :
            low = mid+1             # not the answer 
    
    return ans
    
if __name__ == "__main__":
    arr = [1,2,3,3,5,8,8,10,10,11]
    n = len(arr)
    targets = [1,9]
    
    for target in targets:
        print("The upper bound is : ",upperBound(arr,target,n))
```
- **Time complexity : O(log<sub>2</sub>N)**
- **Space complexity : O(1)**

<br>

## Searching Insert Position in a Sorted Array

- Given a sorted array, and a target value `m`, find the target element in the array, if present, and return it's index.
- If the element is not present then, insert the value at it's correct position and return that index.

### Algorithm 

1. The problem is similar to saying that we need to find the lower bound of the arry. 
2. We implement Lower bound algo and find the location of the target if it exists.

### Code 

```python 
def getInsertionIndex(arr,n,target):
    low = 0
    high = n-1
    ans = n
    
    while low<=high:
        mid = (low+high)//2
        if target<=arr[mid] : 
            ans = mid
            high = mid-1
        else:
            low = mid+1
    arr.insert(ans,target)
    return ans

if __name__=="__main__":
    arr = [1,2,4,7]
    targets = [2,6]
    for target in targets:
        print("The index of insertion of Target is : ",getInsertionIndex(arr,len(arr),target))
        print(arr)
```
- **Time complexity : O(log<sub>2</sub>N)**
  - That is if we ignore the inserting step and only return an index
  - Have done it here just for the understanding
- **Space complexity : O(1)**

<br>

## Floor and Ceil in Sorted Array

- Floor = largest number in a array that is >= x
- Ceil = smallest number in a array that is <= x

### Algorithm

1. The definition of Ceil is exactly same as lower bound. 
2. Hence a simple lower bound function for Ceil
3. The change being that we need to return the number here (for both floor and ceil)
4. For floor, we will have change out lower bound implementation a little bit (just change the sign, rest is the same)

### Code

```python
def calc_floor(arr,n,target):
    low = 0
    high = n-1
    ans = -1
    
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=target:
            ans = arr[mid]
            low = mid+1
        else:
            high = mid-1
    
    return ans

def calc_ceil(arr,n,target):
    low = 0 
    high = n-1
    ans = -1
    
    while low<=high:
        mid = (low+high)//2
        if target<=arr[mid]:
            ans = arr[mid]
            high = mid-1
        else :
            low = mid+1

    return ans

if __name__ == "__main__":
    arr = [10,20,30,40,50]
    xs = [25,20]
    for x in xs:
        floor = calc_floor(arr,len(arr),x)
        ceil = calc_ceil(arr,len(arr),x)
        print("Floor value is : ",floor)
        print("Ceil value is : ",ceil)
```
- **Time complexity : O(log<sub>2</sub>N)**
- **Space complexity : O(1)**