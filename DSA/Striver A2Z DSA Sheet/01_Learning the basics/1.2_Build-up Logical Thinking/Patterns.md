# Patterns 

- Knowing your loops is critical to mastering DSA problems because almost every question needs one.
- Understanding patterns in DSA helps you to understand loops.


<br>

- Pattern questions will require **nested loops**
- Hence there will be a 
  - `Outer loop` (rows / lines)
  - `Inner loop` (columns)

---

## Steps to printing any pattern problem : 

1. For the `outer loop`, count the number of lines
2. for the `inner loop`, focus on the columns and try to connect it to the rows 
3. Print the required character in the `inner loop`
4. Observe the symmetry (optional - not applicable to all)

---

## Pattern questions :

### 1. Print Matrix of nxm :

>- **Problem Statement:** Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.
>- For every value of ‘N’, help sam to print the corresponding N-dimensional forest.

**Example:**
```
Input: ‘N’ = 3
Output: 
* * *
* * *
* * *
```
- **Code**
```python 
def nForest(n:int) ->None:
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()
```

---

### 2. Triangle Pattern 

**Problem Statement:** Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

An N/2-dimensional forest is represented by the lower triangle of the pattern filled with ‘*’.

For every value of ‘N’, help sam to print the corresponding N/2-dimensional forest.
Example:
```
Input:  ‘N’ = 3
Output: 
* 
* *
* * *
```
- **Code**
```python 
def nForest(n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()
```
```python
def nForest(n:int) ->None:
    for i in range(n):
        print('* '*(i+1))
```

### 3. Number Triangle Pattern

>- **Problem Statement:** Sam is making a Triangular painting for a maths project.
>- An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers starting from 1.
>- For every value of ‘N’, help sam to print the corresponding N-dimensional Triangle.
- **Example:**
```
Input: ‘N’ = 3
Output: 
1
1 2 
1 2 3
```
- **Code**
```python 
def nTriangle(n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print(f"{j+1}",end=' ')
        print()
```
