def median(matrix,m,n):
    low = float('inf')
    high = float('-inf')

    # Assign low and high values 
    # By checking the first and last col elements of the matrix
    # cuase the rows are sorted, the lowest values will be in col[0] and highest values of the rows will be in col[n-1]
    for i in range(m):
        low = min(low,matrix[i][0])
        high = max(high,matrix[i][n-1])
    
    # Our required number : 
    req = (n*m)//2
    
    # Binary Search
    while low<=high:
        mid = (low+high)//2
        elements_less_than_equal = BlackBox(matrix,n,m,mid)
        if elements_less_than_equal <= req:
            low = mid+1
        else:
            high = mid-1
    return low

def BlackBox(matrix,n,m,mid):
    '''
    returns the number of elements in the matrix <= mid
    '''
    count=0
    # go row wise and BS the row for upper bound of mid
    # Upper bound will retunr the index of the number just greator than mid
    # This giving is the exact count of elements <= mid
    for i in range(m):
        count+=upperBound(matrix[i],n,mid)
    return count

def upperBound(arr,n,x):
    low = 0
    high = n-1
    ans = n

    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            ans = mid       # maybe an answer 
            high=mid-1
        else:               # looking for a smaller index on the left 
            low = mid+1
    return ans

if __name__=="__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [8, 9, 11, 12, 13],
        [21, 23, 25, 27, 29]
    ]
    m = len(matrix)
    n = len(matrix[0])
    ans = median(matrix, m, n)
    print("The median element is:", ans)