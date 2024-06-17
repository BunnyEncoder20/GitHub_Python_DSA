# Pascals Triangle

## Variation 1 : Finding Element at Position(row,col)

- Given a row and col, find the element of the Pascal's Triangle at that position. 

>- Formula for calculating the element at a given position(row,col) in pascal triangle is **nCr (n!/r!x(n-r)!)**
>- Where : n = row -1 and r = col-1

- The calculation of the nCr can be optimized by removing the parts of the factorial which will get cancelled out anyways between the n! and the (n-r)!.
- Eg: Assuming row = 5 and col = 3
- nCr = n! / (r! * (n-r)!) 
- 5-1C3-1 = 4! / 2! * (4- 2)! = 4 * 3 * (2*1) / (2 * 1) * (2 * 1) = (4x3) / (2x1)
- As we saw the numerator ran for only (r) number of times (or col-1), 
- **NOTE:** when calculating the numerator and denominator, it is better that the denominator be iterated over from 1 to r. Numerator can be the same as before (n to 1). So the faction should follow the below order (for correct calculation of int nCr)
```
4 x 3 
-----
2 x 1
```
- So we can optimize the loop for the calculation of the answer as follows: 

```python
for i in range (r):
    ans *= (n-i)    # Numerator
    ans //= (i+1)   # Denominator
```

---

## Variation 2 : Finding nth row of Pascals Triangle

- Another variation of the problem is to find the nth row of the Pascals Triangle.
- This can done by 
>- Running a loop for the number of row (cause row number = number of elements in that row) and calling a function to do the nCr (Brute Force approach) [ Time complexity : O(nxr) ]
- Thi can be optimized by noticing that the elements of the row follow a pattern.
- The formula to calculate the elements go in the order :
- Assume the n = 6th row 
- First and last element will always be = 1
```
The 2nd element will be:
5
---
1

The 3rd element will be
5 x 4 
-----
1 x 2

The 4th element will be
5 x 4 x 3
---------
1 x 2 x 3

And so on...
```
- Each element adds something more to the previous fraction 
- Specifically the answer will get multiplied by (n-i) [ or row-col ] and divided by (i+1) [ col ]
- Basically : 
```
element = previousElement * (row-col) / col
```
- Hence the Time complexity will be optimized to **`O(n)`**
- Hence the formula for calculating the row elements one after another can be : 
  
```python
for j in range (1,row-1):
        result = ansRow[j-1] * (row-j)
        result = result // (j)
        ansRow[j] = result
```

---

## Variation 3 : Printing entire Pascal's Triangle

- Brute force approach to this problem would be to use the <sup>n</sup>C<sub>r</sub> function to calculate the elements of the row and keep adding the rows to the result list. 

```python
ans = []
for(row=1 -> n):
    temp = []
    for(col=1 -> row):
        temp.append(nCr(row-1,col-1))
return ans
```
- The time complexity is some what like : O(n x n x r) 
- Which is approx (not exactly) = **O(n<sup>3</sup>)**

<br>

- Instead of using the first solution (to calculate each element), instead we will use the 2nd solution (to calculate the entire row using our optimal formal for row elements).
- This will reduce the Time complexity to **O(n<sup>2</sup>)** which is the optimized solution for this problem.

```python
ans = []
for(row=1 -> n):
   ans.append(calcRow(row))
return ans
```
- Below is a example of the code for the same : 

```python
def getRow(n:int):
    middleElements = [0]*n-2
    rowElements = [1,*middleElements,1]
    
    for j in range(1,n-1):
        temp = rowElements[j-1] * (n-j)
        temp = temp // j
        rowElements[j] = temp
        
    return rowElements

def printPascal(row:int):
    ans = []
    for i in range(row):
        ans.append(getRow(i+1))

    return ans

if __name__ == '__main__':
    row = int(input("row: "))
    pascalTriangle = printPascal(row)
    
    print(f"Pascal's Triangle for {row} rows:")
    for row in pascalTriangle:
        print(row)
```

---