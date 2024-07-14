from collections import defaultdict

def get_nse(arr,n):
    stack = []
    ans = defaultdict(lambda:-1)
    
    for i in range(n-1,-1,-1):
        if not stack:
            stack.append(arr[i])
        elif stack[-1] < arr[i] :
            ans[arr[i]] = stack[-1]
            stack.append(arr[i])
        elif stack[-1] >= arr[i]:
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                ans[arr[i]] = stack[-1]
            stack.append(arr[i])
    res = [ans[num] for num in arr]
    return res

if __name__ == "__main__":
    arr = [4,8,5,2,25]
    res = get_nse(arr,len(arr))
    print(*res)