from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue 
            else:
                j = i+1
                k = n-1
                
                while j<k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        ans.append([nums[i],nums[j],nums[k]])
                        j+=1
                        k-=1
                        
                        while nums[j]==nums[j-1] and j<k : j+=1
                        while nums[k]==nums[k-1] and j<k : k-=1

                    elif sum<0:
                        j+=1
                    elif sum>0:
                        k-=1 
        
        return ans

if __name__ == "__main__":
    i = Solution()
    numsList = [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]]
    
    for nums in numsList : 
        print(i.threeSum(nums))