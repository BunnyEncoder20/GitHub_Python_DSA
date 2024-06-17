# 
# Brute Force Approach 
# Time complexity : O(n^3)
# 


from typing import List

class Solution:
    def mark_row(self, matrix, row):
        for j in range(len(matrix[0])):
            if matrix[row][j] != 0:
                matrix[row][j] = -1 
    
    def mark_col(self, matrix, col):
        for i in range(len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = -1
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    self.mark_row(matrix,i)
                    self.mark_col(matrix,j)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

if __name__=='__main__':
    instance1 = Solution()
    mat1 = [[1,1,1],[1,0,1],[1,1,1]]
    mat2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    listOfMatrixes = [mat1, mat2]
    
    for matrix in listOfMatrixes:
        instance1.setZeroes(matrix)
    
    print(mat1)
    print(mat2)
