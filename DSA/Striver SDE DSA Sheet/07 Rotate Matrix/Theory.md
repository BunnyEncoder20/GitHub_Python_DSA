# Rotate Matrix (Rotate Image)

- Given a matrix of nxn, print what the matrix will be if it were rotated by 90 degrees.
- Eg: 
![alt text](mat1.jpg)
**Input:** matrix = \[[1,2,3],[4,5,6],[7,8,9]]
**Output:** \[[7,4,1],[8,5,2],[9,6,3]]

---

## Brute Force

- **Time Complexity : O(n<sup>2</sup>)**
- **Space Complexity : O(n<sup>2</sup>)**

<br>

- by looking at the indexes of the matrix , we can figure out a pattern between the rows and columns
- [const][j] --maps to->  [j][const]
- Eg: 
  - [0][0] becomes [0][3]
  - [0][1] becomes [1][3]
  - [0][2] becomes [2][3]
  - [0][3] becomes [3][3]
- Similarly, the next row : 
  - [1][0] becomes [0][2]
  - [1][1] becomes [1][2]
  - [1][2] becomes [2][2]
  - [1][3] becomes [3][2]
- Hence the pattern can be :


> [i][j] becomes [j][(n-1)-i]

- Code : 

```python
# Brute force solution for matrix rotation
# Time complexity : O(n^2)
# Space complexity : O(n^2)

from typing import List 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        answer = [[0 for x in range(n)] for y in range(n)]  # create a answer mat of size n x n initialized to 0
        
        for i in range(n):
            for j in range(n):
                answer[j][(n-1)-i] = matrix[i][j]
                # print(answer)
        
        return answer
        
if __name__ == "__main__":
    ins = Solution()
    
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    
    print(ins.rotate(matrix1))
    print(ins.rotate(matrix2))
```

--- 

## Optimal Solution

- **Time Complexity : O(n<sup>2</sup>)**
- **Space Complexity : O(1)**
- This approach is considered better as we do in space replacement. That way, the space complexity is reduced. 
- The observation which helps to solve this:
  - The first column = first row BUT in reverse order. 
  - The Second column = second row BUT in reverse order.
  - The third column = third row BUT in reverse order.
  - The forth column = forth row BUT in reverse order.
- Hence we need to Transpose the matrix.
- If we observe then all the elements of the diagonal are the same
- And all the other elements have swapped places with their diagonal counterpart elements.

<br>

- Steps of Algorithm:
1. Transpose : 

```python
for i in range(0,n-1):
    for j in range(i+1,n):
        swap(a[i][j], a[j][i])
```
2. Reverse all the rows of the answer mat

```python
for row in a:
    row.reverse()
```

- Code : 

```python 
from typing import List 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Making transpose
        for i in range(0,n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        # Reversing the rows
        for row in matrix:
            row.reverse()
    

if __name__ == '__main__':
    ins = Solution()
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    
    ins.rotate(matrix1)
    ins.rotate(matrix2)
    
    print(matrix1)
    print(matrix2)
```

---

