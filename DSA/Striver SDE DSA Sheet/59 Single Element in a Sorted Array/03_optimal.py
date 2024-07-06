def singleNonDuplicate(arr):
    n = len(arr)

    # Edge cases 
    # there is only one element
    if n==1 : return arr[0]    
    # Check the first element
    if arr[0]!=arr[1] : return arr[0]
    # Check the last element 
    if arr[n-1]!=arr[n-2] : return arr[n-1]

    # Binary search for remaining elements
    low = 1
    high = n-2

    while low<=high:
        mid = (low+high)//2
        if arr[mid-1]!=arr[mid] and arr[mid]!=arr[mid+1] : 
            return arr[mid]
        
        # single element is on the right half
        # first condition if we on a odd index then the left should be the same number 
        # second condition if we on an even index then the right number should be the same
        elif (mid%2==1 and arr[mid-1]==arr[mid]) or (mid%2==0 and arr[mid]==arr[mid+1]):
            low = mid+1
        
        # single element is on the left half
        else:
            high = mid-1

    # Dummy return (will never execute as answer is gauranteed)
    return -1
if __name__=="__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    ans = singleNonDuplicate(arr)
    print("The single element is:", ans)