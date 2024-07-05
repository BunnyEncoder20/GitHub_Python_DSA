def NthRoot(n,m)->int:
    low,high = 1,m
    # Binary Search 
    while low<=high:
        mid = (low+high)//2
        if pow(mid,n,m)==0: return mid
        elif pow(mid,n,m)==1 : low=mid+1
        else: high=mid-1
    return -1

# def pow(base,expo,m):
#     '''
#     returns  1 : ans<m
#     returns  0 : ans==m
#     returns -1 : ans>m
#     '''
#     ans = 1
#     for _ in range(expo):
#         ans*=base
#         if ans>m : return -1
#     if ans==m : return 0
#     else : return 1

def pow(base,n,m):
    ans = 1
    while n>0:
        if n%2==0:
            base*=base
            n//=2
        else:
            ans*=base
            if ans>m : return -1
            n-=1
    if ans == m : return 0
    else : return 1
    

if __name__ == "__main__":
    listn = [3,4]
    listm = [27,69]
    n,m=0,0
    while n<len(listn) and m<len(listm):
        # print(f"n:m::{listn[n]}:{listm[m]}")
        print("The answer is:",NthRoot(listn[n], listm[m]))
        n+=1
        m+=1