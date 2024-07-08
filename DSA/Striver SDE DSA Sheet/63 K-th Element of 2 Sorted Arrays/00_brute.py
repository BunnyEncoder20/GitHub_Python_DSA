def kthElement(arr1, arr2, n1, n2, x):
    left = 0
    right = 0
    temp = []
    while left<n1 and right<n2:
        if arr1[left]<=arr2[right]:
            temp.append(arr1[left])
            left+=1
        else:
            temp.append(arr2[right])
            right+=1
    if left<n1 : temp.extend(arr1[left:])
    if right<n2 : temp.extend(arr2[right:])
    
    return temp[x-1]
        

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    print("The k-th element of two sorted arrays is:", kthElement(a, b, len(a), len(b), 5))