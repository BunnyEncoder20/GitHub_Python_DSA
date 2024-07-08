def median(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    # To ensure that the smallest array is arr1
    if n1>n2 : return median(arr2, arr1)

    low = 0
    high = n1 
    req_on_left = (n1+n2+1)//2
    n = n1+n2    
    # Binary serach the number of elements we need to take on the left
    while low<=high:
        mid1 = (low+high)//2
        mid2 = req_on_left - mid1

        # elements near the symmtric line default values
        l1,l2 = float('-inf'),float('-inf')
        r1,r2 = float('inf'),float('inf')

        # Check that the index exist before assigning the values to the edge elements 
        if mid1 < n1 : r1 = arr1[mid1]
        if mid2 < n2 : r2 = arr2[mid2]
        if mid1-1 >= 0 : l1 = arr1[mid1-1]
        if mid2-1 >= 0 : l2 = arr2[mid2-1]

        # Checking if this is the symmertric we have been looking for 
        if l1<=r2 and l2<=r1 : 
            if n%2==1 : 
                # assuming there are more elements on the left side
                return float(max(l1,l2))
            else:
                return float(max(l1,l2)+min(r1,r2))/2.0

        # move to the left 
        elif l1 > r2 : high = mid1-1
        else : low = mid1+1 

    return 0 

if __name__ == "__main__":
    # a = [1, 4, 7, 10, 12]
    # b = [2, 3, 6, 15]
    a = []
    b = [1]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))