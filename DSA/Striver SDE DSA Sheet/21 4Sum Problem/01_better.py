from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        answerSet = set()

        for i in range(n):
            for j in range(i+1,n):
                hashmap = set()
                for k in range(j+1,n):
                    l = target - (nums[i] + nums[j] + nums[k])
                    
                    if l in hashmap:
                        quadruplets = [nums[i],nums[j],nums[k],l]
                        quadruplets.sort()
                        answerSet.add(tuple(quadruplets))
                    
                    hashmap.add(nums[k]) 
        
        return [list(quadruplets) for quadruplets in answerSet]

if __name__ == "__main__":
    i = Solution()
    nums1,t1 = [1,0,-1,0,-2,2],0
    nums2,t2 = [2,2,2,2,2],8

    print(i.fourSum(nums1,t1))
    print(i.fourSum(nums2,t2))