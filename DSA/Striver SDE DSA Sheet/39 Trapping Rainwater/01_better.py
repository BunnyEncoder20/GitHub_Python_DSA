from typing import List 

def trap(arr:List[int]):
    n = len(arr)
    prefix = [0]*n
    suffix = [0]*n 

    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = max(prefix[i-1],arr[i])
    suffix[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        suffix[i] = max(suffix[i+1],arr[i])
    trapped_rainwater = 0
    for i in range(n):
        trapped_rainwater+=min(prefix[i],suffix[i])-arr[i]
    return trapped_rainwater


if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {trap(arr)}")
