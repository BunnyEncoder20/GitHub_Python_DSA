def getRow(n:int):
    middleElements = [0]*n-2
    rowElements = [1,*middleElements,1] # this is the spread operator for python
    
    for j in range(1,n):
        temp = rowElements[j-1] * (n-j)
        temp = temp // j
        rowElements[j] = temp
        
    return rowElements

def printPascal(row:int):
    ans = []
    for i in range(row):
        ans.append(getRow(i+1))
    return ans

if __name__ == '__main__':
    row = int(input("row: "))
    pascalTriangle = printPascal(row)
    
    print(f"Pascal's Triangle for {row} rows:")
    for row in pascalTriangle:
        print(row)
        

