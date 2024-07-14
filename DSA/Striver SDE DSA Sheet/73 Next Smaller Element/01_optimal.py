def get_nse(arr, n):
        # Your code goes here
        # Return the list
        stack = []
        nse = [-1]*n
        
        for i in range(n-1,-1,-1):
            if not stack:
                stack.append(arr[i])
            elif stack and stack[-1]<arr[i]:
                nse[i] = stack[-1]
                stack.append(arr[i])
            elif stack and stack[-1]>=arr[i]:
                while stack and stack[-1]>=arr[i]:
                    stack.pop()
                if stack : 
                   nse[i] = stack[-1]
                stack.append(arr[i])
        
        return nse

if __name__ == "__main__":
    arr = [2 ,5 ,3 ,7 ,1 ,5 ,2 ,6 ,3,1]
    res = get_nse(arr,len(arr))
    print(*res)