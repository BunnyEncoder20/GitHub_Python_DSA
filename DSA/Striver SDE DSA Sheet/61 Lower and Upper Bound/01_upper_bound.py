def upperBound(arr,target,n):
    low = 0 
    high = n-1
    ans = n
    
    while low<=high:
        mid = (low+high)//2         # There are again only 2 possibilities here

        if target<arr[mid] :        
            ans = mid               # this might be the answer 
            high = mid-1
        else :
            low = mid+1             # not the answer 
    
    return ans
    
if __name__ == "__main__":
    arr = [1,2,3,3,5,8,8,10,10,11]
    n = len(arr)
    targets = [1,9]
    
    for target in targets:
        print("The upper bound is : ",upperBound(arr,target,n))