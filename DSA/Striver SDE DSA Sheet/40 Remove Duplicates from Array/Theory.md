# Find 2<sup>nd</sup> Largest Element in a Array | Remove Duplicates from a sorted Array

## Largest Element in a Array

### Brute Force Approach 

- Sort the array
- return last element

### Code 

```python 
def getLargest(arr):
    arr.sort()
    return arr[len(arr)-1]
```
- **Time complexity : O(nlogn)**
- **Space complexity : O(1)**

### Optimal Approach 

- take a largest = a[0]
- iterate over the arr and update largest when needed

### Code 

```python
def optimal_getLargest(arr):
    largest = arr[0]
    for i in range(1,len(arr)):
        largest = max(arr[i],largest)
    return largest
```

- **Time complexity :  O(n)**
- **Space complexity : O(1)**

---

## 2<sup>nd</sup> Largest Element in Array

### Brute Force Approach 
- sort the array 
- assign last element as largest
- iterate backwards till you find an element which is not the largest.

### Code

```python
def second_largest(arr):
    n = len(arr)
    arr.sort()
    largest = arr[n-1]
    index = n-1
    while largest==arr[index]:
        index-=1
    return arr[index] if index>=0 else -1
```

- **Time complexity : O(nlogn) + O(n)**
- **Space complexity : O(1)**

### Better Approach 

- Find the largest element in first pass
- in next pass find largest which is not equal to largest 

### Code 

```python 
def better_second_largest(arr):
    n = len(arr)
    largest,second_largest = -1,-1

    for i in range(n):
        largest = max(arr[i],largest)
    for i in range(n):
        if arr[i]>=second_largest and arr[i]!=largest:
            second_largest = arr[i]
    return second_largest
```
- **Time complexity : O(n) + O(n) = O(2n)**
- **Space complexity : O(1)**


### Optimal Approach 

- largest = arr[0] and second_largest = -1
- itreate over the array and update the largest
- when largest is updated, second_largest will become the previous largest
- Even if element is not greater than largest, we must check with second largest

### Code 

```python
def optimal_second_largest(arr):
    n = len(arr)
    slargest = float('-inf')
    largest = arr[0]

    for i in range(n):
        if arr[i]>largest:
            slargest = largest
            largest = arr[i]
        elif largest>arr[i] and arr[i]>slargest:
            slargest = arr[i]
        else:
            continue
    return slargest if slargest != float('-inf')
```
- Time complexity : O(n)
- Space complexity : O(1)

--- 

## Check if a Array is sorted 

```python
def checkSort(arr):
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:continue
        else: return False
    return True
```
- **Time complexity : O(n)**
- **Space complexity : O(1)**

---

## Remove Duplicates from a Sorted Array

- Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once.
- The relative order of the elements should be kept the same.


### Brute Force Approach 

- [Watch it here](https://youtu.be/37E9ckMDdTk?si=1YyZYoDjwbHuWqHC)
- Put all the elements into the a set DS
- return the length of the set

```python 
def check_duplicates(arr):
    uniques = set()
    for num in arr:
        uniques.add(num)
    return len(uniques)

if __name__ == '__main__':
    arr = [1,1,2,2,2,3,3]
    print(check_duplicates(arr))
```
- **Time complexity : O(nlogn) + O(n)**
- **Space complexity : O(n)**

### Optimal Approach 

- [Watch it here](https://youtu.be/37E9ckMDdTk?si=uSq3jDhSp5Gc_Hai&t=2255)
- Using the 2 poiner approach 
- Fix i and keep moving j until it is not equal to i
- when encountering another number, we assign it the position in front of i and move i to that position.

### Code 

```python
def optimal_check_duplicates(arr):
    n = len(arr)
    i = 0
    for j in range(1,n):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i+=1
    return i+1
```
- **Time complexity : O(n)**
- **Space complexity : O(1)**

---
---