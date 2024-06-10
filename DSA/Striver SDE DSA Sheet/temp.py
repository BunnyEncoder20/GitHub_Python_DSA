class Solution:
    def printPascals(self, row):
        ans = []
        for i in range(row):
            ans.append(self.getRow(i+1))
        return ans
    
    def getRow(self, i):
        row = [0]*i
        row[0] = 1
        
        for j in range(1,i):
            row[j] = ((row[j-1]*(i-j))/j) 
        
        return row

if __name__ == '__main__':
    i = Solution()
    row = 6
    print(i.printPascals(row))