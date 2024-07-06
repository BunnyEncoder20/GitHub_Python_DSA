# Search Single Element in a sorted array

- Given an array of `N` integers.
- Every number in the array except one appears twice. Find the single number in the array.
- Examples : 
```
Example 1:
Input Format:
 arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Result:
 4
Explanation:
 Only the number 4 appears once in the array.
```
```
Example 2:
Input Format:
 arr[] = {1,1,3,5,5}
Result:
 3
Explanation:
 Only the number 3 appears once in the array. 
```
- **Note** there will always be a single element and the remaining elements will be occuring twice 

<br>

## Brute Force Approach 1

### Algorithm 

- [Watch it here](https://youtu.be/AZOmHuHadxQ?si=s2y8-RiHJ-ICvcGo&t=94)
- If we are at a index i then i-1 or i+1 should have the same element
- If not, then we return that element cause it is single

### Code 

```python 
def singleNonDuplicate(arr):
    n = len(arr)
    # edge case : if there is only one element in the input array
    if n==1:
        return arr[0]

    for i in range(n):
        # first element
        if i == 0:
            if arr[i+1]!=arr[i] : return arr[i]
        # last element
        elif i==n-1:
            if arr[i-1]!=arr[i] : return arr[i]
        # middle elements
        else:
            if arr[i-1]!=arr[i] and arr[i]!=arr[i+1]:
                return arr[i]

if __name__=="__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    ans = singleNonDuplicate(arr)
    print("The single element is:", ans)
```
- **Time complexity : O(n)**
- **Space complexity : O(1)**

<br>

## Brute Force Approach 2 

- We can use XOR operations to find the number which is not being dulicated by using the following properties : 
    1. a^0 = a : anything XOR with 0 is itself
    2. a^a = 0 : anything XOR with itself, results in 0

### Algorithm 

1. We loop through the array and XOR all the elements
2. The one which doesn't get cancelled out by it;s duplicate will only be left in the end. 

### Code 

```python 
def singleNonDuplicate(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans ^= arr[i]
    return ans

if __name__=="__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    ans = singleNonDuplicate(arr)
    print("The single element is:", ans)
```
- Time complexity : O(n)
- Space complexity : O(1)

<br>

## Optimal Approach 

- As we are given a array which is sorted, we can apply binary search

### Algorithm 

1. [Watch it here](https://youtu.be/AZOmHuHadxQ?si=N7O-8JNHcgzt1bVs&t=344)
2. Based on the index being odd or even , we can determine which have the single element is in.
    - (even,odd) implies that element is on the right half
    - (odd,even) implies that element is on the left half
3. Check every mid for being the single element
4. If we reduce the serach space to (1,n-2) to avoid the edge cases of index being out of range for checking the left and right element


### Code 

```python
def singleNonDuplicate(arr):
    n = len(arr)

    # Edge cases 
    # there is only one element
    if n==1 : return arr[0]    
    # Check the first element
    if arr[0]!=arr[1] : return arr[0]
    # Check the last element 
    if arr[n-1]!=arr[n-2] : return arr[n-1]

    # Binary search for remaining elements
    low = 1
    high = n-2

    while low<=high:
        mid = (low+high)//2
        if arr[mid-1]!=arr[mid] and arr[mid]!=arr[mid+1] : 
            return arr[mid]
        
        # single element is on the right half
        # first condition if we on a odd index then the left should be the same number 
        # second condition if we on an even index then the right number should be the same
        elif (mid%2==1 and arr[mid-1]==arr[mid]) or (mid%2==0 and arr[mid]==arr[mid+1]):
            low = mid+1
        
        # single element is on the left half
        else:
            high = mid-1

    # Dummy return (will never execute as answer is gauranteed)
    return -1
if __name__=="__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    ans = singleNonDuplicate(arr)
    print("The single element is:", ans)
```
- **Time complexity : O(log<sub>2</sub>N)**
- **Space complexity : O(1)**

---
---