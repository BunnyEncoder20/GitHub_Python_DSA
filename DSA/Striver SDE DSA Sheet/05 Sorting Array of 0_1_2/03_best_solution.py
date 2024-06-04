# Dutch National Flag Algorithm 
# Time Complexity : O(N)
# Space Complexity : O(1)

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,mid,high = 0,0,len(nums)-1

        while mid <= high :
            
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid] 
                mid+=1
                low+=1

            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
                
        

if __name__ == '__main__':
    nums1,nums2 = [2,0,2,1,1,0] , [2,0,1]
    sol = Solution()
    sol.sortColors(nums1)
    sol.sortColors(nums2)
    print(nums1)
    print(nums2)