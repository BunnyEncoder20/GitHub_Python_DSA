def element_at_position(row:int):
    ansRow = [0]*row 
    ansRow[0],ansRow[-1]=1,1
    result = 1
    
    for j in range (1,row-1):
        result = ansRow[j-1] * (row-j)
        result = result // (j)
        ansRow[j] = result
    
    return ansRow

if __name__ == '__main__':
    row = int(input("row: "))
    # col = int(input("col: "))
    print("Ans:",element_at_position(row))