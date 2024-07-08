def kthElement(arr1, arr2, n1, n2, x):
    if n1>n2 : return kthElement(arr2,arr1,n2,n1,x)
    
    n = n1+n2
    req_left = x
    low = max(0,x-n2)
    high = min(n1,x)
    
    while low<=high:
        mid1 = (low+high)//2
        mid2 = req_left - mid1
        
        if mid1 < n2 : r1 = arr1[mid1]
        if mid2 < n2 : r2 = arr2[mid2]
        if mid1-1>=0 : l1 = arr1[mid1-1]
        if mid2-1>=0 : l2 = arr2[mid2-1]

        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1>r2 :
            high = mid-1
        else:
            low = mid+1

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))