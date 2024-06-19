from typing import List 

def trap(arr:List[int]):
    n = len(arr)
    total_water = 0 
    for i in range(n):
        left_max = arr[i]
        right_max = arr[i]

        j = i
        while j>=0:
            left_max = max(left_max,arr[j])
            j-=1
        # reset j
        j=i
        while j<n:
            right_max = max(right_max,arr[j])
            j+=1
        total_water += min(left_max, right_max) - arr[i]

    return total_water


if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {trap(arr)}")
