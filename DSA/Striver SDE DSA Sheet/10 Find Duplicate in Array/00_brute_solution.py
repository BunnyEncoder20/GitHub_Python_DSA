from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                dup = nums[i]
                break
        
        return dup
    
if __name__ == "__main__":
    List_of_nums = [[1,3,4,2,2],[3,1,3,4,2],[3,3,3,3,3]]
    ins = Solution()
    
    for nums in List_of_nums:
        print(ins.findDuplicate(nums))