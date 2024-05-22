def element_at_position(row:int,col:int) -> int:
    n = row-1
    r = col-1
    ans = 1
    
    for i in range (r):
        ans *= (n-i)
        ans //= (i+1)
    
    return ans

if __name__ == '__main__':
    row = int(input("row: "))
    col = int(input("col: "))
    print("Ans:",element_at_position(row,col))