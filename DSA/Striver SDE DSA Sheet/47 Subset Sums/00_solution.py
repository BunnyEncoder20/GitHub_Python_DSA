from typing import List 

class Solution:
    def subsetSums(self,arr:List[int],n:int)->List[int]:
        answer = []

        def subsetSumHelper(index,sum):
            if index==n:
                answer.append(sum)
                return

            # The element is picked 
            subsetSumHelper(index+1,sum+arr[index])

            # The element is not picked
            subsetSumHelper(index+1,sum)
        
        subsetSumHelper(0,0)
        answer.sort()
        return answer

if __name__ == "__main__":
    arr = [3, 1, 2]
    ans = Solution().subsetSums(arr, len(arr))
    print("The sum of each subset is")
    for sum in ans:
        print(sum, end=" ")
    print()