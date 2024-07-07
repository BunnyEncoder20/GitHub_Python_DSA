def getInsertionIndex(arr,n,target):
    low = 0
    high = n-1
    ans = n
    
    while low<=high:
        mid = (low+high)//2
        if target<=arr[mid] : 
            ans = mid
            high = mid-1
        else:
            low = mid+1
    arr.insert(ans,target)
    return ans

if __name__=="__main__":
    arr = [1,2,4,7]
    targets = [2,6]
    for target in targets:
        print("The index of insertion of Target is : ",getInsertionIndex(arr,len(arr),target))
        print(arr)