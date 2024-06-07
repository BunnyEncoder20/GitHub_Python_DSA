from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        element = None

        for i in range(n):
            if count == 0 :
                element = nums[i]
                count = 1
            elif nums[i]==element :
                count+=1
            else:
                count-=1

        elementCounter = 0
        for i in range(n):
            if nums[i]==element:
                elementCounter+=1
        if elementCounter > n//2 :
            return element
        else : 
            return -1


if __name__ == "__main__":
    nums1 = [3,2,3]
    nums2 = [2,2,1,1,1,2,2]
    i = Solution()

    print(i.majorityElement(nums1))
    print(i.majorityElement(nums2))