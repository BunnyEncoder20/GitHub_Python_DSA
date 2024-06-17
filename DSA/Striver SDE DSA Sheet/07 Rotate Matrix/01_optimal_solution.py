# Optimal Solution for Matrix Rotation 
# Time Complexity : O(n/2 * n/2) + O(n * n/2)
# Space Complexity : O(1)

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