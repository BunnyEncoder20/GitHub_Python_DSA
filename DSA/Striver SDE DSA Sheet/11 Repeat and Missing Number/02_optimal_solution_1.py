from typing import List

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        
        S = 0
        Sn = (n*(n+1))//2
        S2 = 0
        Sn2 = (n * (n+1) * (2*n+1)) // 6
        
        for i in range(n):
            S += A[i]           
            S2 += A[i]*A[i]
        
        # Assuming x is repeating number 
        # Assuming y is missing number 
        val1 = S-Sn             # x-y
        val2 = (S2-Sn2) // 2    # x+y = (S2-Sn2)/(x-y)
        
        x = (val1+val2)//2
        y = val2-x
        
        return [x,y]

if __name__ == '__main__':
    A = [3, 1, 2, 5, 3]
    ins = Solution()
    print(ins.repeatedNumber(A))    # Ans : [3,4]