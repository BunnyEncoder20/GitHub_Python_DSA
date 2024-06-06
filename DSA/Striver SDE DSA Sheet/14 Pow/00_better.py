class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        nn = n      # original n
        

        if nn < 0 : nn = abs(nn)
    
        while nn > 0 : 
            if nn%2 == 0 :
                x *= x
                nn = nn//2
            else : 
                ans *= x
                nn -= 1
        
        return ans if n > 0 else 1/ans

if __name__ == "__main__":
    i = Solution()
    x1,x2,x3 = 2.00000,2.10000,2.00000
    n1,n2,n3 = 10,3,-2

    print(i.myPow(x1,n1))
    print(i.myPow(x2,n2))
    print(i.myPow(x3,n3))