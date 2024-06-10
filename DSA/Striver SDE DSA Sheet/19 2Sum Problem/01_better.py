from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            require = target-nums[i]
            if require in hashmap:
                return [hashmap[require],i]
            else:
                hashmap[nums[i]] = i 
        


if __name__ == "__main__":
    nums1,t1 = [2,7,11,15],9
    nums2,t2 = [3,2,4],6
    nums3,t3 = [3,3],6

    i = Solution()
    print(i.twoSum(nums1,t1))
    print(i.twoSum(nums2,t2))
    print(i.twoSum(nums3,t3))