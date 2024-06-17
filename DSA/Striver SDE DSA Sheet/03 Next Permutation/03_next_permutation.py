# Optimal Solution for Next Permutation 
# Time Complexity : O(n)
# Space Complexity : O(1) [in-place modification]

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Step 1) Finding the breakpoint
        breakpoint = -1
        n = len(nums)
        
        for i in range(n-2,-1,-1):  
            if(nums[i]<nums[i+1]):
                breakpoint = i
                break
        
        if breakpoint == -1:
            nums.reverse()
            return
        
        
        # Step 2) Swapping breakpoint digit with one which is just greater than it on the right side
        for i in range(n-1,breakpoint,-1):
            if(nums[i]>nums[breakpoint]):
                nums[i],nums[breakpoint]=nums[breakpoint],nums[i]
                break   # don't forget this break
                
        # Step 3) reversing the digits on the right side of the breakpoint to get next permutation
        nums[breakpoint+1:] = reversed(nums[breakpoint+1:])
        


if __name__=="__main__":
    list_of_numbers = [[1,3,2],[1,3,8,7,6,4,2]]
    classInstance = Solution()
    
    for num in list_of_numbers:
        num = classInstance.nextPermutation(num)
    
    for num in list_of_numbers:
        print(num)