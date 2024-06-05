from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq_arr = [0]*len(nums)

        for num in nums:
            if freq_arr[num] == 1:
                return num 
            else:
                freq_arr[num] = 1
    
if __name__ == "__main__":
    List_of_nums = [[1,3,4,2,2],[3,1,3,4,2],[3,3,3,3,3]]
    ins = Solution()
    
    for nums in List_of_nums:
        print(ins.findDuplicate(nums))