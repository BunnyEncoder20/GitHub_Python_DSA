from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        answerSet = set()

        for i in range(n):
            for j in range(i+1,n):
                hashset = set()
                for k in range(j+1,n):
                    forth = target - (nums[i]+nums[j]+nums[k])

                    if forth in hashset:
                        tempList = [nums[i],nums[j],nums[k],forth]
                        tempList.sort()
                        answerSet.add(tuple(tempList))
                        
                    hashset.add(nums[k])
        
        return [list(quadruplets) for quadruplets in answerSet]

if __name__ == "__main__":
    i = Solution()
    nums1,t1 = [1,0,-1,0,-2,2],0
    nums2,t2 = [2,2,2,2,2],8

    print(i.fourSum(nums1,t1))
    print(i.fourSum(nums2,t2))