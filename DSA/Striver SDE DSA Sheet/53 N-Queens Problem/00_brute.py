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