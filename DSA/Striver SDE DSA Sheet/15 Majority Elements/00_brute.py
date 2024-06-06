from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j] : count+=1
            if count > (n//2) : 
                return nums[i]

        return -1
            


if __name__ == "__main__":
    nums1 = [3,2,3]
    nums2 = [2,2,1,1,1,2,2]
    i = Solution()

    print(i.majorityElement(nums1))
    print(i.majorityElement(nums2))