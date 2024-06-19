def max_consecutive_1s(arr):
    n = len(arr)
    max_length = 0
    counter = 0

    for i in range(n):
        if arr[i] == 1:
            counter+=1
            max_length = max(max_length,counter)
        else:
            counter = 0
    return max_length

if __name__ == '__main__':
    arr1 = [1,1,0,1,1,1]
    arr2 = [1,0,1,1,0,1]
    print(max_consecutive_1s(arr1))
    print(max_consecutive_1s(arr2))