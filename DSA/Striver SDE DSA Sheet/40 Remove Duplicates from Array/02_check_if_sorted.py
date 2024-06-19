def checkSort(arr):
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:continue
        else: return False
    return True

if __name__ == '__main__':
    arr1=[1,2,2,3,3,4]
    arr2=[1,2,1,3,4]
    print(checkSort(arr1))
    print(checkSort(arr2))