def calc_floor(arr,n,target):
    low = 0
    high = n-1
    ans = -1
    
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<=target:
            ans = arr[mid]
            low = mid+1
        else:
            high = mid-1
    
    return ans

def calc_ceil(arr,n,target):
    low = 0 
    high = n-1
    ans = -1
    
    while low<=high:
        mid = (low+high)//2
        if target<=arr[mid]:
            ans = arr[mid]
            high = mid-1
        else :
            low = mid+1

    return ans

if __name__ == "__main__":
    arr = [10,20,30,40,50]
    xs = [25,20]
    for x in xs:
        floor = calc_floor(arr,len(arr),x)
        ceil = calc_ceil(arr,len(arr),x)
        print("Floor value is : ",floor)
        print("Ceil value is : ",ceil)