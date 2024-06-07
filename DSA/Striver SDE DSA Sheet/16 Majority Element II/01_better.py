from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashmap = {}
        ans = []
        atleast = (n//3) + 1

        for i in range(n):

            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else : 
                hashmap[nums[i]] += 1

            if hashmap[nums[i]] == atleast:
                ans.append(nums[i])
            
            if len(ans) == 2 : break 
        
        return ans
                    


if __name__ == "__main__":
    listNums = [[3,2,3],[1],[1,2]]
    i = Solution()
    for num in listNums:
        print(i.majorityElement(num))