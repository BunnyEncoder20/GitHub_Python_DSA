# N-Queens Problem

- The n-queens is the problem of placing `n` queens on `n × n` chessboard such that no two queens can attack each other. 
- Given an integer `n`, return all distinct solutions to the n -queens puzzle. 
- Each solution contains a distinct boards configuration of the queen's placement, where ‘Q’ and ‘.’ indicate queen and empty space respectively.
- Examples : 
```
Examples:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```
![alt text](<pasted image 0.png>)

<br>

## Brute Approach (Back Tracking)

### Algorithm
- [Watch it here](https://youtu.be/i05Ju7AftcM?si=LApUVnGJpB8tbkjJ&t=415)
- check for each col and each row, if we can place a Q there.
- If we find a place, we all the Q to that place and move to the next col
- if we cannot place a Q in any row, then that sequence is wrong and we pop that sequence 
- else if we are able to place all n Q then that is a correct sequence and we can append it into the answer
- Recursive go back and make the stack empty 

### Code

```python
from typing import List 

class Solution:
    def solveNQueens(self,n):
        ans = []
        board = ['.'*n for _ in range(n)]
        self.solve(board,0,ans,n)
        return ans

    def solve(self,board,col,ans,n):
        if col==n:
            ans.append(board[:])
            return
        
        for row in range(n):
            if self.isSafe(board,row,col,n):
                # if safe, place a Queen
                board[row] = board[row][:col]+'Q'+board[row][col+1:]
                self.solve(board,col+1,ans,n)
                # After the recusion, remove the Queen
                board[row] = board[row][:col]+"."+board[row][col+1:]
    
    def isSafe(self,board,row,col,n):
        row_copy = row
        col_copy = col
        
        # As we are going col wise, 
        # We need to only check the left side of the board
        
        # Check the left upper diagonal 
        while row>=0 and col>=0:
            if board[row][col]=='Q': return False
            row-=1
            col-=1
            
        # Check the left siide of the row
        row = row_copy
        col = col_copy
        while col>=0:
            if board[row][col]=='Q':return False
            col-=1

        # Check the left lower diagonal
        row = row_copy
        col = col_copy
        while row<n and col>=0:
            if board[row][col]=='Q':return False
            row+=1
            col-=1
        
        return True
    
if __name__ == "__main__":
    n = 4
    obj = Solution()
    ans = obj.solveNQueens(n)
    for i in range(len(ans)):
        print(f"Arrangement {i+1}")
        for j in range(len(ans[0])):
            print(ans[i][j])
        print()
```
- **Time complexity : O(n! * n)**
  - Exponential as we are trying out all the possibilities recursively.
- **Space complexity : O(n<sup>2</sup>)**
  - O(n<sup>2</sup>) for the board
  - O(n<sup>2</sup>) for the ans 
  - O(n) auxiliary recursive space complexity
  - = O(n<sup>2</sup>) + O(n<sup>2</sup>) + O(n) = O(n<sup>2</sup>)

<br>

## Optimal Approach (Hashing)

- [Watch it here](https://youtu.be/i05Ju7AftcM?si=8BONWp6zoFnTiuMW&t=1726)
- We can optimize the isSafe function by using hashing instead of checking for all  upper diagonal, left of row and lower diagonal elements.
- (n) size list for the leftRow hash
- (2n-1) size list for the upperLeftDiagonal
- (2n-1) size list for the lowerLeftDiagonal
- For the lower left diagonal, we can add the row+col to get the hash index. 
- For the upper left diagonal, we can use the formula : `(n-1)+(col-row)` to get the hash index

### Code 

```python 
from typing import List 

class Solution:
    def solveNQueens(self,n):
        board = ['.'*n for _ in range(n)]
        left_row = [0]*n
        left_upper_diagonal = [0]*(2*n-1)
        left_lower_diagonal = [0]*(2*n-1)
        ans = []
        self.solve(board,0,ans,n,left_row,left_upper_diagonal,left_lower_diagonal)
        return ans

    def solve(self,board,col,ans,n,left_row,left_upper_diagonal,left_lower_diagonal):
        if col==n:
            ans.append(board[:])
            return

        for row in range(n):
            if not left_row[row] and not left_upper_diagonal[(n-1)+(col-row)] and not left_lower_diagonal[row+col]:
                # Place the Queen
                board[row] = board[row][:col]+"Q"+board[row][col+1:]
                left_row[row] = 1
                left_lower_diagonal[row+col] = 1
                left_upper_diagonal[(n-1)+(col-row)] = 1
                self.solve(board,col+1,ans,n,left_row,left_upper_diagonal,left_lower_diagonal)
                # Remove the Queen
                board[row] = board[row][:col]+"."+board[row][col+1:]
                left_row[row] = 0
                left_lower_diagonal[row+col] = 0
                left_upper_diagonal[(n-1)+(col-row)] = 0
        
    
if __name__ == "__main__":
    n = 4
    obj = Solution()
    ans = obj.solveNQueens(n)
    for i in range(len(ans)):
        print(f"Arrangement {i+1}")
        for j in range(len(ans[0])):
            print(ans[i][j])
        print()
```
- **Time complexity : (n! * n)**
  - Exponential because we are still checking every possible placement of Queen recursively.
  - Times n for each col
- **Space complexity : O(n<sup>2</sup>)**
  - O(n<sup>2</sup>) for board
  - O(n) for Hashs
  - O(n) auxiliary space complexity 