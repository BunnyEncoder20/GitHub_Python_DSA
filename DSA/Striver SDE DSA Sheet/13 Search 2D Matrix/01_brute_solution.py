from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target : return True
        
        return False

if __name__ == "__main__":
    ins = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    target2 = 13
    print(ins.searchMatrix(matrix,target1))
    print(ins.searchMatrix(matrix,target2))