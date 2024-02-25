def nStarDiamond(n: int) -> None:
    spaces = n-1
    stars = 1

    for i in range(n*2):
        for j in range(spaces):
            print(' ',end='')
        for j in range(stars):
            print('*',end='')
        print()
        if(i<=n//2):
            spaces-=1
            stars+=2
        else:
            spaces+=1
            stars-=2

        
if __name__ == '__main__':
    nStarDiamond(4)