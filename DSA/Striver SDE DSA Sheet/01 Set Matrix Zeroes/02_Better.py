# 
# Better Approach 
# Time complexity : O(nxm)
# Space complexity : O(n) + O(m)
# 


from typing import List

class Solution:
            
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rowChk = [0]*rows
        colChk = [0]*cols
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowChk[i] = 1
                    colChk[j] = 1

        for i in range(rows):
            for j in range(cols):
                if rowChk[i] or colChk[j]:
                    matrix[i][j] = 0

if __name__=='__main__':
    instance1 = Solution()
    mat1 = [[1,1,1],[1,0,1],[1,1,1]]    
    mat2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    listOfMatrixes = [mat1, mat2]
    
    for matrix in listOfMatrixes:
        instance1.setZeroes(matrix)
    
    print(mat1) # Correct answer = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(mat2) # Correct answer = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
