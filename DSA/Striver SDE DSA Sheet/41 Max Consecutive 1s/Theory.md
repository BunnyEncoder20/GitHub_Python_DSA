# Max Number of Consecutive 1s

- Given a binary array nums, return the maximum number of consecutive 1's in the array.
- Exmaples :

**Example 1:**
> Input: nums = [1,1,0,1,1,1]
> Output: 3
> Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

**Example 2:**
> Input: nums = [1,0,1,1,0,1]
> Output: 2

<br>

## The only Approach 

- It is a small and simple problem
- probably a warmup or follow to an actual problem

### Algorithm 

- count = 0 and max_length = 0
- iterate over the array and increase the counter and whenever counter updates, also update the max_length
- When again 0 is encountered, we reser the counter

### Code 

```python 
def max_consecutive_1s(arr):
    n = len(arr)
    max_length = 0
    counter = 0

    for i in range(n):
        if arr[i] == 1:
            counter+=1
            max_length = max(max_length,counter)
        else:
            counter = 0
    return max_length

if __name__ == '__main__':
    arr1 = [1,1,0,1,1,1]
    arr2 = [1,0,1,1,0,1]
    print(max_consecutive_1s(arr1))
    print(max_consecutive_1s(arr2))
```
- **Time complexity : O(n)**
- **Space complexity : O(1)**