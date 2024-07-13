from typing import List 

class Solution:
    def nextGreaterElements(self,arr:List[int]) -> List[int]:
        n = len(arr)
        stack = []
        nge = [-1]*n
        for i in range(2*n-1,-1,-1):
            index = i%n
            
            # remove all the elements which were lower than the current element
            while stack and stack[-1] <= arr[index]:
                stack.pop()
            
            # Assign the top to the nge array
            if i<n : 
                if stack:
                    nge[i] = stack[-1]
            
            # push the element into the stack
            stack.append(arr[index])

        return nge
            
if __name__ == '__main__':
    obj = Solution()
    v = [5, 7, 1, 2, 6, 0]
    res = obj.nextGreaterElements(v)
    print("The next greater elements are")
    print(*res)