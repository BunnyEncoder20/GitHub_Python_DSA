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
                
        
        return answer
        
if __name__ == "__main__":
    ins = Solution()
    
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    
    print(ins.rotate(matrix1))
    print(ins.rotate(matrix2))
    
    