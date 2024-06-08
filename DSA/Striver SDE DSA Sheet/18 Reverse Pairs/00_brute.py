from typing import List 

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        counter = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] > 2*nums[j] : counter+=1
        
        return counter
    
if __name__ == "__main__":
    i = Solution()
    listNums = [[1,3,2,3,1],[2,4,3,5,1]]
    for nums in listNums : 
        print(i.reversePairs(nums))