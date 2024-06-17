def getInversions(arr,n):
    counter = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j] : counter+=1
    
    return counter

if __name__ == "__main__":
    arr1, n1 = [3,2,1],3
    arr2, n2 = [2, 5, 1, 3, 4],5
    arr3, n3 = [52244275, 123047899, 493394237, 922363607, 378906890, 188674257, 222477309, 902683641, 860884025, 339100162],10
    
    print(getInversions(arr1, n1))  # 3
    print(getInversions(arr2, n2))  # 4
    print(getInversions(arr3, n3))  # 16