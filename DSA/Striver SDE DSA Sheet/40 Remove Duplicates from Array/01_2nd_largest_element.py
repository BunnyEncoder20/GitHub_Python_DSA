# Brute Force Approach
def second_largest(arr):
    n = len(arr)
    arr.sort()
    largest = arr[n-1]
    index = n-1
    while largest==arr[index]:
        index-=1
    return arr[index]

# Better Approach 
def better_second_largest(arr):
    n = len(arr)
    largest,second_largest = -1,-1

    for i in range(n):
        largest = max(arr[i],largest)
    for i in range(n):
        if arr[i]>=second_largest and arr[i]!=largest:
            second_largest = arr[i]
    return second_largest

# Optimal Approach
def optimal_second_largest(arr):
    n = len(arr)
    slargest = float('-inf')
    largest = arr[0]

    for i in range(n):
        if arr[i]>largest:
            slargest = largest
            largest = arr[i]
        elif largest>arr[i] and arr[i]>slargest:
            slargest = arr[i]
    return slargest if slargest != float('-inf') else None
        

if __name__ == "__main__":
    arr = [1,2,4,7,7,5]
    print(second_largest(arr))
    print(better_second_largest(arr))
    print(optimal_second_largest(arr))