from typing import List 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        longest = 0
        streak = 0
        last_smaller = float('-inf')

        for i in range(n):
            if nums[i]-1 == last_smaller : 
                streak+=1
                last_smaller = nums[i]
            elif nums[i]-1 != last_smaller : 
                streak = 0
                last_smaller = nums[i]
            else : # for nums[i]==last_smaller, we do not do anything, just incraese the counter
                continue
            
            longest = max(longest,streak)

if __name__ == "__main__":
    numsList = [[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]]
    i = Solution()
    
    for nums in numsList :
        print(i.longestConsecutive(nums))