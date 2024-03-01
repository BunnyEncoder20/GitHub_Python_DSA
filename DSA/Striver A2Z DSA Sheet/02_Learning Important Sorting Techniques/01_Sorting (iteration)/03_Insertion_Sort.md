# Insertion Sort 

> Takes an element and places it in it's correct position in the array 

<br>


- Consider the following array : 
```python 
[13,46,24,52,20,9]
```

<br>

## Steps
1. Start by defining an initial sorted section in the front of the array : 

```python 
[ 13, 46 | 24,52,20,9 ]
```
2. Are the elements in the sorted section in there correct places ? If not, 'insert' the latest member (the last element in the sorted section) into it's correct place

```python 
[ 13, 46 | 24,52,20,9 ]  # already in correct places
```
3. Add the next element into the sorted section and repeat steps 1 and 2 

```python 
[ 13, 46, 24 | 52,20,9 ]
[ 13, 24, 46 | 52,20,9 ]    # in correct places now
```
4. Repeat the steps 1 to 3 until all the elements are in the sorted section 

```python 
[ 13, 24, 46, 52 | 20,9 ]
[ 13, 24, 46, 52, 20 | 9 ]
[ 13, 20, 24, 46, 52 | 9 ]
[ 13, 20, 24, 46, 52, 9 | ]
[ 9, 13, 20, 24, 46, 52 | ]
[ 9, 13, 20, 24, 46, 52 ]   # Array sorted
```

## Implementation 


## Complexity