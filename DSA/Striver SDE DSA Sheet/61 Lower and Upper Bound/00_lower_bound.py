def lowerBound(arr,target,n):
    low = 0
    high = n-1
    ans = n
    
    while low<=high:
        mid = (low+high)//2     # there are only 2 possibilities : 
        
        if arr[mid]>=target:    # this might be an answer 
            ans = mid
            high = mid-1
        else :                  # or not the answer
            low = mid+1
            
    return ans

if __name__ == "__main__":
    arr = [1,2,3,3,5,8,8,10,10,11]
    n = len(arr)
    targets = [1,9]
    
    for target in targets:
        print("The lower bound is : ",lowerBound(arr,target,n))
         