from typing import List 

class Solution :
    def subsetsWithDup(self,nums:List[int])->List[List[int]]:
        n = len(nums)
        ds = []
        answer = []
        
        # we need the duplicates side by side 
        nums.sort()
        
        def subsetHelper(index:int)->None:
            answer.append(ds[:])

            for i in range(index,n):
                if i>index and nums[i]==nums[i-1]: continue
                ds.append(nums[i])
                subsetHelper(i+1)
                ds.pop()
        
        subsetHelper(0)
        return answer
        
    
if __name__ == "__main__":
    nums = [1, 2, 2, 2, 3, 3]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print("[ ", end="")
    for i in range(len(ans)):
        print("[ ", end="")
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print("]", end="")
    print(" ]", end="")