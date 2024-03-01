# Bubble Sort

>- Bubble Sort is a simple sorting algorithm that compares adjacent elements and swaps them if they are in the wrong order.
>- It kinda pushes the largest elements towards the end of the array.

- Consider the following array : 

```python 
[13,46,24,52,20,9]
```
<br>

### Steps

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

<br>

### Implementation

