def get_nse(arr,n):
    ans = [-1]*n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                ans[i] = arr[j]
                break
    return ans

if __name__ == "__main__":
    arr = [4,8,5,2,25]
    res = get_nse(arr,len(arr))
    print(*res)