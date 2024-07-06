def search(arr, n, target):
    low = 0
    high = n-1

    while low<=high:
        mid = (low+high)//2

        if arr[mid]==target: return mid

        # if left side is sorted : 
        if arr[low]<=arr[mid] : 
            if target in arr[low:mid+1]:
                high = mid-1
            else:
                low = mid+1
        
        # If  right side is  sorted
        else:
            if target in arr[mid:high+1]:
                low = mid+1
            else:
                high = mid-1
    
    # Dummy return cause answer is gauranteed 
    return -1
    
if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)