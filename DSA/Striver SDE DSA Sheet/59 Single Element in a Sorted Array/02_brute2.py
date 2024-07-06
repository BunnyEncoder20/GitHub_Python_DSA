def singleNonDuplicate(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans ^= arr[i]
    return ans

if __name__=="__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    ans = singleNonDuplicate(arr)
    print("The single element is:", ans)