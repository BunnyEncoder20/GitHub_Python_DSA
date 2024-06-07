class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i,j=0,0
        return self.countPaths(i,j,m,n)
    
    def countPaths(self,i,j,m,n):
        # reached the destination
        if i==n-1 and j==m-1 : return 1

        # reached outside the matrix 
        if i>=n or j>=m : return 0

        # remaining cases down+right
        return self.countPaths(i+1,j,m,n) + self.countPaths(i,j+1,m,n)

if __name__ == "__main__":
    i = Solution()
    m1,n1 = 3,7
    m2,n2 = 23,12

    print(i.uniquePaths(m1,n1))
    print(i.uniquePaths(m2,n2))
