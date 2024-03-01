# Bubble Sort

>- Bubble Sort is a simple sorting algorithm that compares adjacent elements and swaps them if they are in the wrong order.
>- It kinda pushes the largest elements towards the end of the array.

- Consider the following array : 

```python 
[13,46,24,52,20,9]
```
<br>

## Steps

1. Take 2 elements at a time from teh beginning of the array:

```python
[ [ 13,46 ] 24,52,20,9 ]
```
2. If the are in sorted order, don't do anything, else swap them.
   
```python 
> [ 13, [ 46,24 ] 52, 20, 9 ]
> [ 13, [ 24,46 ] 52, 20, 9 ]   # swap
```
3. Repeat step 1 and 2 till the end of the array.

```python
> [ 13, 24, [ 46,52 ] 20, 9 ] 
> [ 13, 24, 46, [ 52,20 ] 9]    
> [ 13, 24, 46, [ 20,52 ] 9]    # swap
> [ 13, 24, 46, 20, [ 52,9 ] ]
> [ 13, 24, 46, 20, [ 9,52 ] ]  # swap
```
- This completes one round of Bubble sorting
- Now we can demarcate the last elements as the sorted section of the array. 
- Now we repeat the steps 1 to 3 for the next round but only till **n-2**. 

```python
> [ [ 13,24 ] 46, 20, 9 | 52 ]
> [ 13 [ 24,46 ] 20, 9 | 52 ]
> [ 13, 24, [ 46,20 ] 9 | 52 ]
> [ 13, 24, [ 20,46 ] 9 | 52 ]   # swap
> [ 13, 24, 20, [ 46,9 ] | 52 ]
> [ 13, 24, 20, [ 9,46 ] | 52 ]  # swap
> [ 13, 24, 20, 9, 46 | 52 ] 
> [ 13, 24, 20, 9 | 46, 52 ]     # round 2 completed 
```
- Now repeat steps 1 to 4 till **n + 1** index (the first element will be automatically in the sorted in place) to sort the array.

```python
> [ [ 13,24 ] 20, 9 | 46, 52 ]
> [ 13 [ 24,20 ] 9 | 46, 52 ]
> [ 13 [ 20,24 ] 9 | 46, 52 ]       # swap
> [ 13, 20, [ 24,9 ] | 46, 52 ]
> [ 13, 20, [ 9,24 ] | 46, 52 ]     # swap
> [ 13, 20, 9 | 24, 46, 52 ]        # round 3 completed

> [ [ 13,20 ] 9 | 24, 46, 52 ]
> [ 13 [ 20,9 ] | 24, 46, 52 ]
> [ 13 [ 9,20 ] | 24, 46, 52 ]      # swap
> [ 13, 9 | 20, 24, 46, 52 ]        # round 4 completed 

> [ [ 13,9 ] | 20, 24, 46, 52 ]     # swap
> [ [ 9,13 ] | 20, 24, 46, 52 ]     # round 5 completed 

> [ 9, 13,  20, 24, 46, 52 ]        # Array sorted
```

<br>

## Implementation
- **Remember** that the outer loop needs to go to second last element only 

```python
def bubbleSort(arr):
    for i in range(len(arr)-2, 0, -1):  
        for j in range(i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swap
    return arr
```

<br>

- The above can be optimized by stopping when there are no swaps in the inner loop.

```python
def bubbleSort(arr):
    for i in range(len(arr)-2, 0, -1):  
        didSwap = False
        for j in range(i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swap
                didSwap = True
        if not didSwap:
            break
    return arr
```

## Complexity

| **Case**            	| **Time Complexity** 	|
|-----------------	|-----------------	|
| Average & Worst 	| **O(n<sup>2</sup>)** 	|
| Best            	| **O(n)**            	|
