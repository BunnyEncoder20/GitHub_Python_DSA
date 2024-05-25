from typing import List

def generate(numRows: int) -> List[List[int]]:
    triangle = []

    for i in range(numRows):
        getRow = [0]*(i+1)
        getRow[0],getRow[-1]=1,1
        
        for j in range(1,i+1):
            getRow[j] = getRow[j-1] * ((i+1)-j)
            getRow[j] //= j
        
        triangle.append(getRow)

    return triangle

if __name__ == '__main__':
    print(generate(5))