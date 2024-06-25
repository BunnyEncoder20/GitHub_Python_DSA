from typing import List

class Solution:
    def subsetsWithDup(self,nums:List[int])->List[List[int]]:
        n = len(nums)
        result = set()
        answer = []

        def subsetsHelper(index,current):
            if index==n:
                # current.sort()
                result.add(tuple(current))
                return 
            current.append(nums[index])
            subsetsHelper(index+1,current)
            current.pop()
            subsetsHelper(index+1,current)
        
        subsetsHelper(0,[])
        for element in result:
            answer.append(list(element))
        answer.sort()
        return answer


if __name__ == "__main__":
    nums = [1, 2, 2]
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