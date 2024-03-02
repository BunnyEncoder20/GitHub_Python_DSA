def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i
        while j>0 and arr[j-1]>arr[j] :
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
            
    return arr

if __name__ == '__main__':
    print(insertionSort([9,46,24,52,20,13]))