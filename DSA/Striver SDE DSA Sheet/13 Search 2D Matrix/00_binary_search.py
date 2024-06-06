def binarySearch(arr,n,target):
    low = 0
    high = n-1

    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target :
            return True 
        elif target < arr[mid] :
            high = mid-1
        else : 
            low = mid+1
    
    return False


def recursiveBinarySearch(arr,low,high,target):

    # base case 
    if low>high : return False

    # For all other cases.
    mid = (low+high)//2
    if arr[mid] == target:
        return True
    elif arr[mid] < target :
        return recursiveBinarySearch(arr,mid+1,high,target)
    else : 
        return recursiveBinarySearch(arr,low,mid-1,target)


if __name__ == "__main__":
    arr = [1,3,5,7,10,11,16,20,23,30,34,60]
    t1,t2 = 3,13
    print(binarySearch(arr,len(arr),t1))
    print(binarySearch(arr,len(arr),t2))
    print()
    print(recursiveBinarySearch(arr,0,len(arr)-1,t1))
    print(recursiveBinarySearch(arr,0,len(arr)-1,t2))
