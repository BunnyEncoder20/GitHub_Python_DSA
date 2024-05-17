def pattern(rows:int) -> None:
    star = 1
    
    for row in range(rows):
        startingNum = 1 if row % 2 == 0 else 0

        for j in range(row+1):
            print(startingNum, end=' ')
            startingNum = 1 if startingNum == 0 else 0
        
        print()

if __name__=="__main__":
    pattern(5)