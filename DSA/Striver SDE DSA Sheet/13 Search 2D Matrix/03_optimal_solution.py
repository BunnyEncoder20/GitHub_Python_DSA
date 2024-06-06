from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m*n-1

        while low <= high : 
            mid = (low+high)//2
            row = mid//n
            col = mid%n

            if matrix[row][col] == target : 
                return True 
            elif matrix[row][col] < target : 
                low = mid+1
            else : 
                high = mid-1
        
        return False 
        

if __name__ == "__main__":
    ins = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    target2 = 13
    print(ins.searchMatrix(matrix,target1))
    print(ins.searchMatrix(matrix,target2))