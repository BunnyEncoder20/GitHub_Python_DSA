from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    ans.append(i)
                    ans.append(j)
            if ans : break
                        
        return ans


if __name__ == "__main__":
    nums1,t1 = [2,7,11,15],9
    nums2,t2 = [3,2,4],6
    nums3,t3 = [3,3],6

    i = Solution()
    print(i.twoSum(nums1,t1))
    print(i.twoSum(nums2,t2))
    print(i.twoSum(nums3,t3))
