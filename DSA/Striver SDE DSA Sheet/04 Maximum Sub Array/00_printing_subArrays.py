# Brute Force Maximum Sub Array.

def maxSubArrays(arr):
    n = len(arr)
    maxi = float('-inf')
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
            maxi = max(maxi,sum)
    return maxi

if __name__ == '__main__':
    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    print(maxSubArrays(arr))