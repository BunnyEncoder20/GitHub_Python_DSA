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

---

### 16. Level Letter Right Triangle

- **Pattern**
```
Input: ‘N’ = 3

Output: 
A
B B
C C C
```
- **Code**
```python
def alphaRamp(n: int) -> None:
    char = 65
    for i in range(n):
        for j in range(i+1):
            print(chr(char),end=' ')
        print()
        char+=1
```

---

### 17. Letter Pyramid

- **Pattern**
```
Input: ‘N’ = 3

Output: 
    A
  A B A
A B C B A
```
- **Code**
```python
def alphaHill(n: int):
    bracket = 1
    spaces = n-1
    
    for i in range(n):
        letter = 64
        for j in range(spaces):
            print(' ',end=' ')
        for j in range(bracket):
            if(j <= bracket//2):
                letter+=1
                print(chr(letter),end=' ')
            else:
                letter-=1
                print(chr(letter),end=' ')
        print()
        spaces-=1
        bracket+=2
```

---

### 18. Bottom Letter starting Letter Right Triangle

- **Pattern**
```
Input: ‘N’ = 3

Output: 
C
C B 
C B A
```
- **Code**
```python
def alphaTriangle(n: int):
    
    for i in range(n):
        letter = 65+(n-1)
        for j in range(i+1):
            print(chr(letter),end=' ')
            letter-=1
        print()
```

---

### 19. Symmetric Diamond Void

- **Pattern**
```
Input: ‘N’ = 3

Output: 
* * * * * * 
* *     * * 
*         * 
*         * 
* *     * * 
* * * * * * 
```
- **Code**
```python
def symmetry(n: int):

    # for the Upper Inverted Crown
    spaces = 0
    stars = n
    for i in range(n):
        for star in range(stars):
            print('*',end=' ')
        for space in range(spaces):
            print(' ',end=' ')
        for star in range(stars):
            print('*',end=' ')
        print()
        stars-=1
        spaces+=2
    
    # For the lower crown
    spaces = (n*2)-2
    stars = 1
    for i in range(n):
        for star in range(stars):
            print('*',end=' ')
        for space in range(spaces):
            print(' ',end=' ')
        for star in range(stars):
            print('*',end=' ')
        print()
        stars+=1
        spaces-=2
```

---

### 20. Symmetric BowTie

- **Pattern**
```
Input: ‘N’ = 3

Output: 
*         *
* *     * *
* * * * * *
* *     * *
*         *
```
- **Code**
```python
def symmetry(n: int):
    stars = 1
    spaces = (n*2)-2
    for i in range(n):
        for j in range(stars):
            print('*',end=' ')
        for j in range(spaces):
            print(' ',end=' ')
        for j in range(stars):
            print('*',end=' ')
        print() 
        if i<n-1 :
            stars+=1
            spaces-=2
            
    for i in range(n-1):
        stars-=1
        spaces+=2
        for j in range(stars):
            print('*',end=' ')
        for j in range(spaces):
            print(' ',end=' ')
        for j in range(stars):
            print('*',end=' ')
        print()
```

---

### 21. Rectangle Border of N rows

- **Pattern**
```
Input: ‘N’ = 4

Output: 

****
*  *
*  *
****
```
- **Code**
```python
def getStarPattern(n: int) -> None:
    for i in range(n):
        if (i==0 or i==(n-1)):
            print('*'*n)
        else :
            print('*',end='')
            print(' '*(n-2),end='')
            print('*')
```

---

### 22. Number Matrix (decreeing Numeber towards center)

- **Pattern**
```
Input: ‘N’ = 4

Output: 

4444444
4333334
4322234
4321234
4322234
4333334
4444444
```
>- The **trick** is that the required matrix can be made by doing ( n - minimum distance from edges)
>- **Eg:** we know that the number 1 in above example has a distance of 3 from the top,right,bottom,left edges.
>- These distances can be easily calculated from the indexes of the matrix. 
>- In the same example the 2 to the right of 1 will have the following distances from the edges:
>   - top = 3
>   - right = 2
>   - bottom = 3
>   - left = 4
>- Hence min(top,right,bottom,left) = 2 
>- Hence the required matrix can be made by doing ( n - 2) = (4-2) = 2
- **Code**
```python
def getNumberPattern(n: int) -> None:
    for i in range(n*2-1):
        for j in range(n*2-1):
            top_distance = i
            bottom_distance = (n*2-2)-i
            left_distance = j
            right_distance = (n*2-2)-j
            print(n - min(top_distance, bottom_distance, left_distance, right_distance), end="")
        print()
```