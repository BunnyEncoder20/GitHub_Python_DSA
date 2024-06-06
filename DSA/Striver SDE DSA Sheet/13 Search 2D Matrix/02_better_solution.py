from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = n-1

        for i in range(m):
            if matrix[i][0] <= target and target <= matrix[i][n-1] :
                return self.binarySearch(matrix[i],low,high,target)
    
    def binarySearch(self,arr,low,high,target):

        # base case 
        if low>high : return False

        # remaining case 
        mid = (low+high)//2

        if arr[mid] == target :
            return True 
        elif arr[mid] < target : 
            return self.binarySearch(arr,mid+1,high,target)
        else : 
            return self.binarySearch(arr,low,mid-1,target)


if __name__ == "__main__":
    ins = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    target2 = 13
    print(ins.searchMatrix(matrix,target1))
    print(ins.searchMatrix(matrix,target2))