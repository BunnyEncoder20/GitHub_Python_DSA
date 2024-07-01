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