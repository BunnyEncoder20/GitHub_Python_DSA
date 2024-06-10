from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        uniqueSet = set()

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        sum = nums[i]+nums[j]+nums[k]+nums[l]
                        
                        if sum == target:
                            quadruplets = (nums[i],nums[j],nums[k],nums[l])
                            uniqueSet.add(quadruplets)
        
        return [list(quadruplets) for quadruplets in uniqueSet]



if __name__ == "__main__":
    i = Solution()
    nums1,t1 = [1,0,-1,0,-2,2],0
    nums2,t2 = [2,2,2,2,2],8

    print(i.fourSum(nums1,t1))
    print(i.fourSum(nums2,t2))