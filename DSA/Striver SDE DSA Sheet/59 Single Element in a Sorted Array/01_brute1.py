def singleNonDuplicate(arr):
    n = len(arr)
    # edge case : if there is only one element in the input array
    if n==1:
        return arr[0]

    for i in range(n):
        # first element
        if i == 0:
            if arr[i+1]!=arr[i] : return arr[i]
        # last element
        elif i==n-1:
            if arr[i-1]!=arr[i] : return arr[i]
        # middle elements
        else:
            if arr[i-1]!=arr[i] and arr[i]!=arr[i+1]:
                return arr[i]

if __name__=="__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    ans = singleNonDuplicate(arr)
    print("The single element is:", ans)