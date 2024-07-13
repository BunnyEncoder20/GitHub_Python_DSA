from typing import List
class Solution:
    def nextGreaterElements(self,arr:List[int]) -> List[int]:
        n = len(arr)
        nge = [-1]*n
        
        for i in range(n):
            for j in range(1,n):
                next_index = (i+j)%n
                if arr[i]<arr[next_index]:
                    nge[i] = arr[next_index]
                    break
        return nge

if __name__ == '__main__':
    obj = Solution()
    v = [5, 7, 1, 2, 6, 0]
    res = obj.nextGreaterElements(v)
    print("The next greater elements are")
    print(*res)