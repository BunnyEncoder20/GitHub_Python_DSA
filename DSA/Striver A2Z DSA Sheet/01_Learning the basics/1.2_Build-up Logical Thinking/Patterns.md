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

### 2. Right Triangle Pattern 

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

### 3. Number Right Triangle Pattern

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
---

### 4. Row Number Right Triangle 

- **Pattern**
```
Input: ‘N’ = 3

Output: 
1
2 2 
3 3 3
```
- **Code**
```python 
def triangle( n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print(i+1,end=' ')
        print()
```

--- 

### 5. Inverted Right Triangle

- **Pattern**
```
Input: ‘N’ = 3

Output: 
* * *
* *
*
```
- **Code**
```python
def seeding(n: int) -> None:
    while n>0 :
        for j in range(n):
            print("*",end=' ')
        print()
        n-=1
```
```python 
def seeding(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(n):
            print("*",end=' ')
        print()
        n-=1
```

---

### 6. Inverted Right Number Triangle

- **Pattern**
```
Input: ‘N’ = 3

Output: 
1 2 3
1 2
1
```
- **Code**
```python 
def nNumberTriangle(n: int) -> None:
    for i in range(n,0,-1):
        for j in range(i):
            print(j+1,end=' ')
        print()
```

---

### 7. Star Pyramid 

- **Pattern**
```
Input: ‘N’ = 3

Output: 
  *
 ***
*****
```
- **Code**
```python
def nStarTriangle(n: int) -> None:
    spaces = n-1
    stars = 1
    for i in range(n):
        for s in range(spaces):
            print('',end=' ')
        for j in range(stars):
            print('*',end='')
        print()
        spaces-=1 
        stars+=2
```

--- 

### 8. Inverted Star Pyramid 

- **Pattern**
```
Input: ‘N’ = 3

Output: 
*****
 ***
  *
```
- **Code**
```python
def nStarTriangle(n: int) -> None:
    spaces = 0
    stars = (2*n)-1
    for i in range(n):    
        for j in range(spaces):
            print(' ',end='')
        for j in range(stars):
            print('*',end='')
        spaces += 1
        stars -= 2
        print() 
```

---

### 9. Star Diamond 

- **Pattern**
```
Input: ‘N’ = 3

Output: 

  *
 ***
*****
*****
 ***
  *
```
- **Code**
```python
def nStarDiamond(n: int) -> None:
    spaces = n-1
    stars = 1

    for i in range(n*2):
        for j in range(spaces):
            print(' ',end='')
        for j in range(stars):
            print('*',end='')
        print()
        if(i<=n//2):
            spaces-=1
            stars+=2
        else:
            spaces+=1
            stars-=2

        
if __name__ == '__main__':
    nStarDiamond(4)
```
- (Kinda imperfect cause 2 middle rows, but that is how the CodingNinja question was...)
- I just smashed the Upper pyramid and inverted pyramid together
```python 
def nStarDiamond(n: int) -> None:
    spaces = n-1
    stars = 1

    for i in range(n):
        for j in range(spaces):
            print(' ',end='')
        for j in range(stars):
            print('*',end='')
        print()
        spaces-=1
        stars+=2
    
    spaces = 0
    stars = (2*n)-1

    for i in range(n):
        for j in range(spaces):
            print(' ',end='')
        for j in range(stars):
            print('*',end='')
        print() 
        spaces+=1
        stars-=2
```

---

### 10. Perfect Right Diamond

- **Pattern**
```
Input: ‘N’ = 3

Output: 
*
**
***
**
*
```
- **Code**
```python 
def nStarTriangle(n: int) -> None:
    
    for i in range(n):
        for j in range(i+1):
            print("*",end='')
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print('*',end='')
        print()
        
```

### 11. Binary Right Triangle

- **Pattern**
```
Input: 3

Output:
1 
0 1 
1 0 1
```
- **Code**
```python 
def nBinaryTriangle(n: int) -> None:
    
    for i in range(n):
        binaryOdd = 0
        binaryEven = 1
        for j in range(i+1):
            if i%2==0:
                print(binaryEven,end=' ')
                binaryEven = 0 if binaryEven else 1
            else:
                print(binaryOdd,end=' ')
                binaryOdd = 0 if binaryOdd else 1
        print()
```

### 12. Number Mirrored Crown

- **Pattern**
```
Input: ‘N’ = 3

Output: 
1         1
1 2     2 1
1 2 3 3 2 1
```
- **Code:**
```python 
def numberCrown(n: int) -> None:
    spaces = (n*2)-2
    for i in range(n):
        num=1
        for j in range(i+1):
            print(num,end=' ')
            num+=1
        for j in range(spaces*2):   # x2 to accomodate the spaces created by the prints() in the above and below loop
            print(' ',end='')
        for j in range(i+1):
            num-=1
            print(num,end=' ')
        print()
        spaces-=2
```

---

### 13. Increasing Number Right Triangle

- **Pattern**
```
Input: ‘N’ = 3

Output: 

1
2 3
4 5 6
```
- **Code**
```python
def nNumberTriangle(n: int) -> None:
    num=1
    for i in range(n):
        for j in range(i+1):
            print(num,end=' ')
            num+=1
        print()
```

---

### 14. Increasing Letter Triangle

- **Pattern**
```
Input: ‘N’ = 3

Output: 
A
A B
A B C
```
- **Code**
```python 
def nLetterTriangle(n: int) -> None:
    #chr() returns the  Unicode character of one number
    # A-Z = 65-90
    for i in range(n):
        for j in range(65,65+i+1):
            print(chr(j),end=' ')
        print()
```

--- 

### 15. Increasing Letter Inverted Right Triangle

- **Pattern**
```
Input: ‘N’ = 3

Output: 

A B C
A B
A
```
- **Code**
```python
def nLetterTriangle(n: int):
    # chr() returns Unicode character of one number
    # A-Z = 65-90
    char = n
    for i in range(n):
        for j in range(65,65+char):
            print(chr(j),end=' ')
        print() 
        char-=1
```