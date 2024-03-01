def selectionSort(arr):
    for i in range(0,len(arr)-1):
        mini = arr[i]
        for j in range(i,len(arr)):
            if arr[j] < mini:
                mini = arr[j]
                arr[i],arr[j] = arr[j],arr[i]   # swap
    return arr

if __name__ == '__main__':
    print(selectionSort([9,46,24,52,20,13]))