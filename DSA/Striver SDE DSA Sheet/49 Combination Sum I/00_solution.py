from typing import List 

class Solution:
    def combinationSum(self,candidates:List[int],target:int)->List[List[int]]:
        n = len(candidates)
        answer = []
        ds = []
        
        def combinationHelper(index,target):
            # base cases
            if index==n:
                if target==0 : answer.append(ds[:])
                return
            
            # remaining cases
            # we can only take the index if it is less than target
            if candidates[index]<=target:
                ds.append(candidates[index])
                combinationHelper(index,target-candidates[index])
                ds.pop()
            # else we just move onto the next element
            combinationHelper(index+1,target)
        
        combinationHelper(0,target)
        return answer

if __name__ == "__main__":
    obj = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    ans = obj.combinationSum(candidates, target)
    print("The original candidates are :")
    for num in candidates:
        print(num, end=' ')
    print()
    print("Combinations are: ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()