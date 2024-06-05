# Brute Force Solution
# Time Complexity : O(n^2)
# Space Complexity : O(1)

from typing import List

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        
        for i in range(1,n+1):
            count = 0
            
            for j in range(n):
                if A[j] == i:
                    count += 1
            
            if count == 2: repeating = i
            if count == 0: missing = i
        
        return [repeating, missing]
            

if __name__ == '__main__':
    A = [3, 1, 2, 5, 3]
    ins = Solution()
    print(ins.repeatedNumber(A))
    