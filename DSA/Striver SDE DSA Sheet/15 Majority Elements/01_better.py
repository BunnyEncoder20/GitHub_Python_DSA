from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums : 
            if num in hashmap:
                hashmap[num]+=1
            else : 
                hashmap[num]=1
        
        for key,val in hashmap.items():
            if val > len(nums)//2:
                return key
        
        return -1

if __name__ == "__main__":
    nums1 = [3,2,3]
    nums2 = [2,2,1,1,1,2,2]
    i = Solution()

    print(i.majorityElement(nums1))
    print(i.majorityElement(nums2))