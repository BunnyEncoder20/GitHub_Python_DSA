def getInversions(arr,n):
    return mergeSort(arr,0,len(arr)-1)


def mergeSort(arr,low,high):
    count = 0                       # mod 1
    
    if low>=high : return count     # mod 2
    
    mid = (low+high)//2
    
    count += mergeSort(arr,low,mid)     # mod 3
    count += mergeSort(arr,mid+1,high)  # mod 4
    
    count += merge(arr,low,mid,high)    # mod 5
    
    return count                        # mod 6


def merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp = []
    count = 0                           # mod 7
    
    while left<=mid and right<=high :
        if arr[left] <= arr[right] : 
            temp.append(arr[left])
            left+=1
        else :
            temp.append(arr[right])
            right+=1
            count += (mid-left+1)      # mod 8
        
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    
    for i in range(low,high+1):
            arr[i] = temp[i-low]
        
    return count                # mod 9
            
            
    

if __name__ == "__main__":
    arr1, n1 = [3,2,1],3
    arr2, n2 = [2, 5, 1, 3, 4],5
    arr3, n3 = [52244275, 123047899, 493394237, 922363607, 378906890, 188674257, 222477309, 902683641, 860884025, 339100162],10
    
    print(getInversions(arr1, n1))  # 3
    print(getInversions(arr2, n2))  # 4
    print(getInversions(arr3, n3))  # 16