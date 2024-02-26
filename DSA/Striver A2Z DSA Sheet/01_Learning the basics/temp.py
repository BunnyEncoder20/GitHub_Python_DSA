from math import sqrt
def calcGCD(n:int, m:int)->int:
    while n>0 and m>0:
        if n>m:
            n = n%m
        else :
            m = m%n
    return max(n,m)     # because one of them will be zero, we return the max directly as that will be GCD
    

if __name__ == '__main__':
    print(calcGCD(20,15))