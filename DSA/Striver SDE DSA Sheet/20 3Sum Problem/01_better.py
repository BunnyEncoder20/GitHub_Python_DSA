from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ansSet = set()
        
        for i in range(n):
            hash = set()
            
            for j in range(i+1,n):
                k = 0 - (nums[i]+nums[j])
            
                if k in hash : 
                    temp = [nums[i],nums[j],k]
                    temp.sort()
                    ansSet.add(tuple(temp))

                hash.add(nums[j])
        
        return [list(triplets) for triplets in ansSet]


if __name__ == "__main__":
    i = Solution()
    numsList = [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]]
    
    for nums in numsList : 
        print(i.threeSum(nums))