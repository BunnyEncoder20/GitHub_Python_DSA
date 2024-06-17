# Better solution for sorting a array of 0,1 and 2
# Time Complexity : O(2N)
# Space Complexity : O(1)

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0,count1,count2 = 0,0,0
        
        for num in nums:
            if num == 0:
                count0+=1
            elif num == 1:
                count1+=1
            else :
                count2+=1
        
        for i in range(count0):
            nums[i] = 0
        for j in range(count0,count0+count1):
            nums[j] = 1
        for k in range(count0+count1,count0+count1+count2):
            nums[k] = 2
            
        

if __name__=='__main__':
    nums1,nums2 = [2,0,2,1,1,0] , [2,0,1]
    sol = Solution()
    sol.sortColors(nums1)
    sol.sortColors(nums2)
    print(nums1)
    print(nums2)