# Brute way of finding power(base,expo) TC = O(n)
def NthRoot1(n,m):
    for i in range(m):
        if i**n == m :
            return i
        if i**n > m:
            return -1

# Better way of finding power(base,expo) (less TC = O(log))
def pow(base,expo):
    ans = 1
    while expo>0:
        if expo%2==0:
            base = base**2
            expo//=2
        else:
            ans*=base
            expo-=1
    return ans

def NthRoot2(n,m):
    for i in range(m):
        if pow(i,n)==m : return i
        if pow(i,n)>m  : return -1
    

if __name__ == "__main__":
    listn = [3,4]
    listm = [27,69]
    n,m=0,0
    while n<len(listn) and m<len(listm):
        # print(f"n:m::{listn[n]}:{listm[m]}")
        print("The answer is:",NthRoot2(listn[n], listm[m]))
        n+=1
        m+=1