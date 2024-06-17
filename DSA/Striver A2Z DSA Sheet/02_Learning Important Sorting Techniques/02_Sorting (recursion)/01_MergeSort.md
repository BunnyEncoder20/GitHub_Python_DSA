# Merge Sort

> Merge Sort = Divide and Merge 
- Merge Sort has a much better Time complexity as compared to Bubble, Selection, and Insertion Sort.

- Consider the following array :

```python
arr = [3,1,2,4,1,5,2,6,4]
```
<br>

## Steps 

1. Divide (hypothetically) the array into 2 parts : 

```python
[3,1,2,4,1,5,2,6,4]
[3,1,2,4,1] [5,2,6,4]
```
2. Divide each part again and keep dividing until you have arrays with single elements.

```python
[3,1,2,4,1] [5,2,6,4]
[3,1,2] [4,1]  [5,2] [6,4]
[3,1] [2] [4] [1] [5] [2] [6] [4]
[3] [1] [2] [4] [1] [5] [2] [6] [4]
```

3. Start merging the arrays back in the same order they were divided BUT combine them in a sorted order: 

```python
[3] [1] [2] [4] [1] [5] [2] [6] [4]
[1,3] [2] [4] [1] [5] [2] [6] [4]   # Combine 1 and 3 in sorted order
[1,2,3] [1,4] [2,5] [4,6]
[1,1,2,3,4] [2,4,5,6]
[1,1,2,2,3,4,4,5,6]                 # Sorted
```

4. When combining the arrays, we can take 2 pointers for each of the 2 array begin compared. Compare the elements at the 2 pointers and put the smallest one in the result array and move that pointer forward.
5. If one of the arrays gets over, directly copy the other array's remaining elements into the result array.
6. Repeat this process to get original size array which will be sorted 

<br>

## Implementation & Pseudo Code

- When doing the hypothetical dividing of the array, we are just playing around with the indexes of the array.
- We can take `low` and `high` as the index names which denote the start and end of the hypothetical array. 
- Consider the below **Pseudo Code**

```python

def mergeSort(arr, start, end):

    # Base Case (to stop the recursion)
    if start == end: return 

    # Dividing 
    mid = (start+end)//2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid+1, end)

    # Merging
    merge(arr, start,mid,end)
```
- If still confused watch [this Striver's video](https://youtu.be/ogjf7ORKfd8?si=84IxOxmbPTwNMLGN&t=1505) section

<br>

- **Merge Pseudo Code** 

```python
def merge(arr, start, mid, end):
    left_idx = start    # pointer for left array
    right_idx = mid+1   # pointer for right array
    resultant = []

    while left_idx <= mid and right_idx <= end:
        if arr[left_idx] <= arr[right_idx]:
            resultant.append(arr[left_idx])
            left_idx+=1
        elif arr[left_idx] > arr[right_idx]:
            resultant.append(arr[right_idx])
            right_idx+=1
    
    if not left_idx == mid :
        resultant + arr[left_idx:mid+1]
    if not right_idx == mid:
        resultant + arr[mid+1:end+1]

    # Altering the original array
    for i in range(low,high):
        arr[i] = resultant[i-low]       # be careful of the index of resultant when we copying the elements
```

<br>

- **Python code implementation** 

```python
from typing import List

def merge(arr, start, mid, end):
    left = start
    right = mid+1
    temp = []
    
    while left<=mid and right<=end:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else :
            temp.append(arr[right])
            right+=1
    
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right <= end:
        temp.append(arr[right])
        right+=1

    # if not left == mid:
    #     temp = temp + arr[left:mid+1]
    # if not right == end:
    #     temp = temp + arr[right:end+1]
    
    # Altering the original arr 
    for i in range(start, end+1):
        arr[i] = temp[i-start]
        

def mergeSort(arr, start, end):
    
    # base case : 
    if start == end: return 
    
    
    # Dividing 
    mid = (start + end) // 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid+1, end)
    
    # Merging
    merge(arr, start, mid, end)

if __name__ == '__main__':
    # str = "68 151 175 398 382 369 609 940 982 47 522 497 784 126 659 124 931 272 473 794 411 379 717 502 812 548 50 450 358 136 454 980 916 683 637 317 345 676 899 574 69 201 353 604 588 375 810 119 808 589 53 565 888 929 997 540 649 267 504 727 228 529 53 760 984 114 738 471 290 655 165 234 242 239 721 614 775 138 339 972 509 856 901 320 46 539 266 502 888 18"
    str = "45 216 198 795 484 650 590 431 705 316 557 189 652 606 153 829 813 367 658 961"
    arr = str.split(" ")
    arr = [int(x) for x in arr]
    
    mergeSort(arr, 0, len(arr)-1)
    print(arr)
```

<br>

## Complexity 

- **`Time Complexity`** = **O(nlogn)** 
- For all best,average and worse case 
<br>
- **`Space Complexity`** = **O(n)**