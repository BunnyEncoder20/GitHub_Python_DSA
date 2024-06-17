# Selection Sort

>- Selection Sort 'selects' the minimum in an array and swaps it's position with the first element in the unsorted section of the array. It then makes that index part of the sorted section and only focuses on the remaining array. 
>- You could say it 'selects' the minimum and moves it to the start.
- Consider the below array 

```python
[13,46,24,52,20,9]
```

## Steps

1. select the minimum in the array and exchange it's place with the element at index 0.

```python
[9,46,24,52,20,13]
```
2. Move the start index one step ahead now (include index 0 as that part of the array is sorted now) and find the next smallest element in this new array. 

```python
> [9 | 46,24,52,20,13]
> [9 | 13,24,52,20,46]
```
3. Repeat the above steps till the entire array is in the sorted portion 
   
```python 
> [9,13 | 24,52,20,46]
> [9,13,20 | 52,24,46]
> [9,13,20,24 | 52,46]
> [9,13,20,24,46 | 52]
> [9,13,20,24,46,52]
```
- Notice that we don't need to do the selection sort for the last element as it is already sorted.


## Implementation
  
```python 
for i in range(o to n-1):
    mini = arr[i]
    for j in range(i to n):
        if arr[j] < mini: 
            arr[i],arr[j] = arr[j],arr[i]   # swap the first index and the smallest index
```
- **Do remember** that range(start, end) in python by default goes from start to end-1.

<br>

- **Implementation**
```python
def selectionSort(arr):
    for i in range(0,len(arr)-1):
        mini = arr[i]
        for j in range(i,len(arr)):
            if arr[j] < mini:
                mini = arr[j]
                arr[i],arr[j] = arr[j],arr[i]   # swap
    return arr

if __name__ == '__main__':
    print(selectionSort([9,46,24,52,20,13]))
```

## Complexity 

- **`Time Complexity`** = **O(n<sup>2</sup>)**  
- (for all best, average and worse case)
