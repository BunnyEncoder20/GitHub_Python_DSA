def NthRoot(n,m)->int:
    low,high = 1,m
    # Binary Search 
    while low<=high:
        mid = (low+high)//2
        if pow(mid,n)==m: return mid
        elif pow(mid,n)<m : low=mid+1
        else: high=mid-1
    return -1

def pow(base,expo):
    ans = 1
    while expo>0:
        if expo%2==0:
            base*=base
            expo//=2
        else:
            ans*=base
            expo-=1
    return ans

if __name__ == "__main__":
    listn = [3,4]
    listm = [27,69]
    n,m=0,0
    while n<len(listn) and m<len(listm):
        # print(f"n:m::{listn[n]}:{listm[m]}")
        print("The answer is:",NthRoot(listn[n], listm[m]))
        n+=1
        m+=1