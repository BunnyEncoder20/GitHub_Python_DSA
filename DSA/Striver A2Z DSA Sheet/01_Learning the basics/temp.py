from math import sqrt
def primeCheck(n:int) -> bool :
    factors = 0
    for i in range(1,int(sqrt(n))+1):
        if n%i == 0:
            factors+=1
            if i!=n/i:
                factors+=1
    return True if factors==2 else False

if __name__ == '__main__':
    print(primeCheck(11))