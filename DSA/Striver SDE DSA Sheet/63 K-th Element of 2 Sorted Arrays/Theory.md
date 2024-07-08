# K<sup>th</sup> Element of 2 Sorted Arrays

- Given two sorted arrays of size `m` and `n` respectively, you are tasked with finding the element that would be at the **k<sup>th</sup> position** of the final sorted array. 

<br>

## Brute Force Approach 

- merge the two sorted arrays and then find the K-th element in that merged array.

### Algorithm 

1. Merge the 2 arrays using the merge sort technique 
2. return the k<sup>th</sup> element

### Code

```python 
def kthElement(arr1, arr2, n1, n2, x):
    left = 0
    right = 0
    temp = []
    while left<n1 and right<n2:
        if arr1[left]<=arr2[right]:
            temp.append(arr1[left])
            left+=1
        else:
            temp.append(arr2[right])
            right+=1
    if left<n1 : temp.extend(arr1[left:])
    if right<n2 : temp.extend(arr2[right:])
    
    return temp[x-1]
        

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))
```
- **Time complexity : O(n+m)**
- **Space complexity : O(n+m)**

<br>

## Better Approach 

### Algorithm 

1. Don't store the arr elements in a merged arr.
2. Use a count variable to keep track of the numbers
3. When count = k-1, return that arrs element 

### Code 

```python 
def kthElement(arr1, arr2, n1, n2, x):
    count = 0
    kth = None
    left,right = 0,0
    
    while left<n1 and right<n2:
        if arr1[left]<=arr2[right]:
            if count==x-1 : return arr1[left]
            count+=1
            left+=1
        else:
            if count==x-1 : return arr2[right]
            count+=1
            right+=1
    while left<n1:
        if count==x-1 : return arr1[left]
        left+=1
        count+=1
    while right<n2:
        if count==x-1 : return arr2[right]
        right+=1
        count+=1
    

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))
```
- **Time complexity : O(n+m)**
- **Space complexity : O(1)**

<br>

## Optimal Approach 

- We implement a similar formula as we did when we were solving for median of 2 sorted arrays

### Algorithm 

- [Watch it here](https://youtu.be/D1oDwWCq50g?si=a7FnyyrHoTIAKfys&t=282)
1. Remember to change the conditions for low and high for this problem (K can be larger than the number of elements in the smaller array and also can be very small compared to all the elements of larger arrays)

### Code 

```python 
def kthElement(arr1, arr2, n1, n2, x):
    if n1>n2 : return kthElement(arr2,arr1,n2,n1,x)
    
    n = n1+n2
    req_left = x
    low = max(0,x-n2)
    high = min(n1,x)
    
    while low<=high:
        mid1 = (low+high)//2
        mid2 = req_left - mid1
        
        if mid1 < n2 : r1 = arr1[mid1]
        if mid2 < n2 : r2 = arr2[mid2]
        if mid1-1>=0 : l1 = arr1[mid1-1]
        if mid2-1>=0 : l2 = arr2[mid2-1]

        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1>r2 :
            high = mid-1
        else:
            low = mid+1

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))
```
- **Time complexity : O( log(min(n1,n2)) )**
- **Space complexity : O(1)**

<br>

---
---