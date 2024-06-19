# Brute Force Approach
def getLargest(arr):
    arr.sort()
    return arr[len(arr)-1]

# Optimal Approach
def optimal_getLargest(arr):
    largest = arr[0]
    for i in range(1,len(arr)):
        largest = max(arr[i],largest)
    return largest

if __name__ == "__main__":
    arr = [3,2,1,5,2]
    print(getLargest(arr))
    print(optimal_getLargest(arr))