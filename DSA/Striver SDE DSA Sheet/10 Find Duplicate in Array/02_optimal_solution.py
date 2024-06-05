from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True : 
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow==fast : break
        
        fast = nums[0]

        while slow != fast :
            slow = nums[slow]
            fast = nums[fast]
        
        return slow 

    
if __name__ == "__main__":
    List_of_nums = [[1,3,4,2,2],[3,1,3,4,2],[3,3,3,3,3]]
    ins = Solution()
    
    for nums in List_of_nums:
        print(ins.findDuplicate(nums))