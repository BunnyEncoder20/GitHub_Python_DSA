def kthElement(arr1, arr2, n1, n2, x):
    count = 0
    kth = None
    left,right = 0,0
    
    while left<n1 and right<n2:
        if arr1[left]<=arr2[right]:
            if count==x-1 : return arr1[left]
            count+=1
            left+=1
        else:
            if count==x-1 : return arr2[right]
            count+=1
            right+=1
    while left<n1:
        if count==x-1 : return arr1[left]
        left+=1
        count+=1
    while right<n2:
        if count==x-1 : return arr2[right]
        right+=1
        count+=1
    

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))