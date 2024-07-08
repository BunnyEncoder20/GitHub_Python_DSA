def median(arr1, arr2):
    left = 0
    right = 0
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = []
    
    # Merging the 2 arrays
    while left<n1 and right<n2 :
        if arr1[left]<=arr2[right]:
            arr3.append(arr1[left])
            left+=1
        else:
            arr3.append(arr2[right])
            right+=1

    if left<=n1:
        arr3.extend(arr1[left:])
    if right<=n2:
        arr3.extend(arr2[right:])
    
    # Finding the median in the arr3
    n = n1+n2
    if n%2==1:
        return arr3[n//2]
    else:
        return (arr3[n/2] + arr3[(n/2)-1])/2.0
        
if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))