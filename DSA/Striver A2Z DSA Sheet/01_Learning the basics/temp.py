from math import sqrt
def sumOfAllDivisors(n: int) -> int:
    sumOfAll = 0
    for i in range(1, n + 1):
        for j in range(1, int(sqrt(i))+1):
            if i % j == 0 :
                sumOfAll += j
                if i/j != j:
                    sumOfAll += int(i/j)
            
    return sumOfAll

    
if __name__ == '__main__':
    print(sumOfAllDivisors(3))