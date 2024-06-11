from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        
        for i in range(n):
            if i != 0 and nums[i]==nums[i-1]: continue 
            else : 
                for j in range(i+1,n):
                    if j != i+1 and nums[j]==nums[j-1]: continue
                    else:
                        k = j+1
                        l = n-1
                        
                        while k<l:
                            sum = nums[i] + nums[j] + nums[k] + nums[l]
                            if sum == target:
                                quadruplets = [nums[i],nums[j],nums[k],nums[l]]
                                ans.append(quadruplets)
                                
                                k+=1
                                l-=1
                                while nums[k]==nums[k-1] and k<l : k+=1
                                while nums[l]==nums[l-1] and k<l : l-=1
                            elif sum < target:
                                k+=1
                            elif sum > target:
                                l-=1
        return ans
        
if __name__ == "__main__":
    i = Solution()
    nums1,t1 = [1,0,-1,0,-2,2],0
    nums2,t2 = [2,2,2,2,2],8

    print(i.fourSum(nums1,t1))
    print(i.fourSum(nums2,t2))