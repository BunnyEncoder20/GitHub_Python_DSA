def numberCrown(n: int) -> None:
    spaces = (n*2)-2
    for i in range(n):
        num=1
        for j in range(i+1):
            print(num,end=' ')
            num+=1
        for j in range(spaces*2):
            print(' ',end='')
        for j in range(i+1):
            num-=1
            print(num,end=' ')
        print()
        spaces-=2

        
if __name__ == '__main__':
    numberCrown(3)