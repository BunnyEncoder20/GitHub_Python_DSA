class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n = m+n-2
        r = min(m-1,n-1)     # use the smaller of m-1 or n-1 to reduce the number of calculations
        ans = 1

        for i in range(1,r+1):
            ans = (ans * ((n-r)+i)) // i
            # Be careful of this line 
        
        return ans 

if __name__ == "__main__":
    i = Solution()
    m1,n1 = 3,7
    m2,n2 = 23,12

    print(i.uniquePaths(m1,n1))
    print(i.uniquePaths(m2,n2))