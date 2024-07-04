from typing import List 

class Solution:
    def findPath(self,matrix,n):
        ans = []
        stack = ""
        visited = [[0 for _ in range(4)] for _ in range(4)]
        
        if matrix[0][0]==1:
            self.solve(0,0,matrix,n,stack,visited,ans)
        return ans
    
    def solve(self,i,j,matrix,n,stack,visited,ans):
        if i==n-1 and j==n-1:
            ans.append(stack)
            return
        
        # Downward 
        if i+1 in range(0,n) and not visited[i+1][j] and matrix[i+1][j]==1:
            stack+="D"
            visited[i][j]=1
            self.solve(i+1,j,matrix,n,stack,visited,ans)
            stack=stack[:-1]
            visited[i][j]=0
            
        # Left 
        if j-1 in range(0,n) and not visited[i][j-1] and matrix[i][j-1]==1:
            stack+="L"
            visited[i][j]=1
            self.solve(i,j-1,matrix,n,stack,visited,ans)
            stack=stack[:-1]
            visited[i][j]=0
        
        # Right
        if j+1 in range(0,n) and not visited[i][j+1] and matrix[i][j+1]==1:
            stack+="R"
            visited[i][j]=1
            self.solve(i,j+1,matrix,n,stack,visited,ans)
            stack=stack[:-1]
            visited[i][j]=0
        
        # Upward
        if i-1 in range(0,n) and not visited[i-1][j] and matrix[i-1][j]==1:
            stack+="U"
            visited[i][j]=1
            self.solve(i-1,j,matrix,n,stack,visited,ans)
            stack=stack[:-1]
            visited[i][j]=0
            

if __name__ == '__main__':
    n = 4
    m = [[1, 0, 0, 0], 
         [1, 1, 0, 1], 
         [1, 1, 0, 0], 
         [0, 1, 1, 1]]
    result = Solution().findPath(m, n)
    if len(result) == 0:
        print(-1)
    else:
        for i in range(len(result)):
            print(result[i], end=" ")
    print()