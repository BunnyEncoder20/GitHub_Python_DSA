# Maximum Sub Array (Kadane's Algorithm)

- Sub array is contiguous (continuous) part of an array. 
- The entire array itself and just a single element are also sub array.
- We need to return the maximum sum we can get from a sub array of the given array.

<br>

## Brute

- Trying out all the possible sub arrays of the given array.
- Whichever of those gives the largest sum will be returned.
- Given Below is code for the same:

```python
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
```
- **Time Complexity** = **O(n<sup>3</sup>)**