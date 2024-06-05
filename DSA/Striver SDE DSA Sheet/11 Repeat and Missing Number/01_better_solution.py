from typing import List

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        hashArray = [0]*(n+1)
        
        for num in A:
            hashArray[num] += 1
        
        for i in range(1,len(hashArray)) : 
            if hashArray[i] == 2 : repeated = i
            if hashArray[i] == 0 : missing = i
            
        return [repeated,missing]

if __name__ == '__main__':
    A = [3, 1, 2, 5, 3]
    ins = Solution()
    print(ins.repeatedNumber(A))