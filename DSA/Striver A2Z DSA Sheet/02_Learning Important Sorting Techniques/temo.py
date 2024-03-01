def bubbleSort(arr):
    for i in range(len(arr)-2, 0, -1):  
        didSwap = False
        for j in range(i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swap
                didSwap = True
        if not didSwap:
            break
    return arr

if __name__ == '__main__':
    print(bubbleSort([9,46,24,52,20,13]))