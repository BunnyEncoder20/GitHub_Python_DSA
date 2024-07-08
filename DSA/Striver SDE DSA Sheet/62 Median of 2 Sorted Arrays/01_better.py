def median(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    n = n1+n2
    idx1,idx2 = (n//2)-1, n//2
    count = 0
    ele1 = None
    ele2 = None
    
    # Applly the merge step
    left,right=0,0
    while left<n1 and right<n2 :
        if arr1[left]<=arr2[right]:
            if count==idx1 : 
                ele1 = arr1[left]
            if count==idx2 : 
                ele2 = arr1[left]
                break
            count+=1
            left+=1
        else:
            if count==idx1 : 
                ele1 = arr2[right]
            if count==idx2 : 
                ele2 = arr2[right]
                break
            count+=1
            right+=1

    if not ele1 and not ele2:
        # Do we really need these ? Yes we do. Think about arrays of very unequal sizes
        while left<=n1:
            if count==idx1 : 
                ele1 = arr1[left]
            if count==idx2 : 
                ele2 = arr1[left]
                break    
            left+=1
            count+=1
        while right<=n2:
            if count==idx1 : 
                ele1 = arr2[right]
            if count==idx2 : 
                ele2 = arr2[right]
                break
            right+=1
            count+=1
        
    # Finding the median in the arr3
    if n%2==1:
        return float(ele2)
    else:
        return float(ele1+ele2)/2.0
        
if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))