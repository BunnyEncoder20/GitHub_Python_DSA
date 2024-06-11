from typing import List 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 : return 0

        longest = 0 
        elements = set()    # takes O(1) avg lookup time 

        for i in range(n):
            elements.add(nums[i])
        
        for num in elements:
            if num-1 in elements : 
                continue
            else :
                streak=1
                x = num 
                while x+1 in elements : 
                    x+=1
                    streak+=1
                longest = max(longest,streak)

        return longest


if __name__ == "__main__":
    numsList = [[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]]
    i = Solution()
    
    for nums in numsList :
        print(i.longestConsecutive(nums))