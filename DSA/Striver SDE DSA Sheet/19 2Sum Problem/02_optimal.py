from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left,right = 0,n-1
        nums.sort()

        while left<right:
            sum = nums[left]+nums[right]

            if sum == target : 
                return True
            elif sum < target :
                left+=1
            else:
                right-=1
        
        return False

if __name__ == "__main__":
    nums1,t1 = [2,7,11,15],9
    nums2,t2 = [3,2,4],6
    nums3,t3 = [3,3],6

    i = Solution()
    print(i.twoSum(nums1,t1))
    print(i.twoSum(nums2,t2))
    print(i.twoSum(nums3,t3))