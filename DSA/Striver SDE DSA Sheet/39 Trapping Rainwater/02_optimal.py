from typing import List 

def trap(arr:List[int]):
    n = len(arr)
    left,right = 0,n-1
    left_max,right_max = arr[0],arr[n-1]
    trapped_rainwater = 0

    while left<=right:
        if arr[left]<=arr[right]:
            if left_max <= arr[left]:
                left_max = arr[left]
            else:
                trapped_rainwater += left_max - arr[left]
            left+=1
        else :
            if right_max <= arr[right]:
                right_max = arr[right]
            else:
                trapped_rainwater += right_max - arr[right]
            right-=1
    
    return trapped_rainwater


if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {trap(arr)}")
