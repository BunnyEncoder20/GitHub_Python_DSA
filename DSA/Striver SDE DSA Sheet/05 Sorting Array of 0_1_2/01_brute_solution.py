from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergeSort(nums,0,len(nums)-1)

    def mergeSort(self, nums,low,high):
        if low>=high: return

        mid = (low+high)//2

        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid+1, high)

        self.merge(nums,low,mid,high)
    
    def merge(self, nums,low,mid,high):
        left = low 
        right = mid+1
        temp = []

        while left<=mid and right<=high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1
        
        for i in range(low,high+1):
            nums[i] = temp[i-low]



if __name__ == '__main__':
    nums1,nums2 = [2,0,2,1,1,0] , [2,0,1]
    sol = Solution()
    sol.sortColors(nums1)
    sol.sortColors(nums2)
    print(nums1)
    print(nums2)