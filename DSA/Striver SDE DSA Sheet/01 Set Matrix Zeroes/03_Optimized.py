# 
# Better Approach 
# Time complexity : O(nxm)  (2 x nxm)
# Space complexity : O(1)   (only one variable)
# 

from typing import List

class Solution:
            
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        col0 = matrix[0][0]
        
        # Checking the rows and cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        
                        if  j != 0:
                            matrix[0][j] = 0
                        else :
                            col0 = 0

        # Solving the inner matrix elements 
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        
        # Solving the first row
        if matrix[0][0] == 0:
            for j in range(1,cols):
                matrix[0][j] = 0
        
        # Solving the first col
        if col0 == 0:
            for i in range(rows):
                matrix[i][0] = 0

if __name__=='__main__':
    instance1 = Solution()
    mat1 = [[1,1,1],[1,0,1],[1,1,1]]    
    mat2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    listOfMatrixes = [mat1, mat2]
    
    for matrix in listOfMatrixes:
        instance1.setZeroes(matrix)
    
    print(mat1) # Correct answer = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(mat2) # Correct answer = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
