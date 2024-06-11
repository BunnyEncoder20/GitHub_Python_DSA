from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        n = len(nums)
        
        for i in range(n):
            num = nums[i]
            counter = 1
            
            while num+1 in nums:
                num+=1
                counter+=1
            
            longest = max(longest,counter)
        
        return longest
        

if __name__ == "__main__":
    numsList = [[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]]
    i = Solution()
    
    for nums in numsList :
        print(i.longestConsecutive(nums))