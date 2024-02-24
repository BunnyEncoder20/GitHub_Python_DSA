def nTriangle(n:int) ->None:
    for i in range(n):
        for j in range(i+1):
            print(f"{j+1}",end=' ')
        print()
        
if __name__ == '__main__':
    nTriangle(3)