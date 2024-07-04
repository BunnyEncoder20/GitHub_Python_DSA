class Solution:
    def findPath(self,matrix,n):
        ans = []
        stack = ""
        visited = [[0 for _ in range(n)] for _ in range(n)]
        di = [+1,0,0,-1]
        dj = [0,-1,+1,0]
        
        if matrix[0][0]==1:
            self.solve(0,0,matrix,n,stack,visited,di,dj,ans)

        return ans
    
    def solve(self,i,j,matrix,n,stack,visited,di,dj,ans):
        if i==n-1 and j==n-1:
            ans.append(stack)
            return
        
        # Combining all the four directional ifs into one
        direction = "DLRU"
        for index in range(4):
            nexti = i+di[index]
            nextj = j+dj[index]
            if nexti in range(n) and nextj in range(n) and matrix[nexti][nextj]==1 and not visited[nexti][nextj]:
                visited[i][j]=1

                # Notice how we are creating a new stack everytime we are making the next recursive function call
                self.solve(nexti,nextj,matrix,n,stack+direction[index],visited,di,dj,ans)
                # That also frees us from removing the added direction after the recursive function call
                
                visited[i][j]=0

        

if __name__ == "__main__":
    n = 4
    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    obj = Solution()
    result = obj.findPath(m, n)
    if len(result) == 0:
        print(-1)
    else:
        for i in range(len(result)):
            print(result[i], end=" ")   # DDRDRR DRDDRR
    print()
    