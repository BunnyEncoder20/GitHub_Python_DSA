# The Next Smaller Element

- Given a array, return an answer_array which has the next smaller element (NSE) for each element in the array. 
- Next Smaller element is the first smaller element towards the right of the current element
- If there is no smaller element towards the right, put -1.
- Examples:
```
Input: N = 5, arr[] = {3, 8, 5, 2, 25}
Output: 2 5 2 -1 -1
```
```
Input: N = 4, a[] = {1, 2, 3, 4}
Output: -1 -1 -1 -1 
```

<br>

## Brute Force Approach 

### Algorithm

1. Take 2 pointer approach
2. For each element of the array, check all the elements towards the right to see if any any element smaller.
3. Break after first smaller element

### Code 

```python
def get_nse(arr,n):
    ans = [-1]*n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                ans[i] = arr[j]
                break
    return ans

if __name__ == "__main__":
    arr = [4,8,5,2,25]
    res = get_nse(arr,len(arr))
    print(*res)
```
- Time complexity : O(n<sup>2</sup>)
- Space complexity : O(n)
  - for the ans array

<br>

## Optimal Approach 

- We can optimize our approach using the stack DS
- Approach is similar to NGE problem

### Algorithm 

1. Similar to the NGE stack approach, we start from the back
2. If the stack top is less than current element, then that is the most recent lesser number towards the right
3. If the stack top is greater than current element, then keep popping stack elements till the top is lesser 
4. If after popping, top is present, then add it in the ans array.

### Code 

```python 
def get_nse(arr,n):
    ans = [-1]*n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                ans[i] = arr[j]
                break
    return ans

if __name__ == "__main__":
    arr = [4,8,5,2,25]
    res = get_nse(arr,len(arr))
    print(*res)
```
- Time complexity : O(n)
- Space complexity : O(n)

<br>

---
---