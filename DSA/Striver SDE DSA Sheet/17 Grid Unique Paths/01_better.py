class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        hashtable = [[-1 for i in range(n)] for j in range(m)]
        i,j=0,0
        return self.countPaths(i,j,m,n,hashtable)
    
    def countPaths(self,i,j,m,n,hashtable):
        if i==m-1 and j==n-1: return 1 
        if i>=m or j>=n : return 0 

        # If the value of that state there in the hashtable, return that value else calculate it recursively
        if hashtable[i][j]!=-1 : 
            return hashtable[i][j]
        else : 
            hashtable[i][j] = self.countPaths(i+1,j,m,n,hashtable) + self.countPaths(i,j+1,m,n,hashtable)
            return hashtable[i][j]
    
if __name__ == "__main__":
    i = Solution()
    m1,n1 = 3,7
    m2,n2 = 23,12

    print(i.uniquePaths(m1,n1))
    print(i.uniquePaths(m2,n2))