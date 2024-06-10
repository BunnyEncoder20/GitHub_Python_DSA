from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answerSet = set()

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        answerSet.add(tuple(temp))
                    


        return [list(triplets) for triplets in answerSet]


if __name__ == "__main__":
    i = Solution()
    numsList = [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]]
    
    for nums in numsList : 
        print(i.threeSum(nums))