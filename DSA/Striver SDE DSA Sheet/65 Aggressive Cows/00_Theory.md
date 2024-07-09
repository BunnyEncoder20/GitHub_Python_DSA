# Aggressive Cows 

- [Watch it here](https://youtu.be/R_Mfw4ew-Vo?si=-aF6xUkfAtg1FpUi&t=142)
- You are given an array `arr` of size `n` which denotes the position of stalls.
- You are also given an integer `k` which denotes the number of aggressive cows.
- You are given the task of assigning stalls to '`k`' cows such that the minimum distance between any two of them is the maximum possible.
- Find the maximum possible minimum distance.
- **NOTE** this problem is from the category of `min_of_max` or `max_of_min` category

```
Example 1:

Input Format:
 N = 6, k = 4, arr[] = {0,3,4,7,10,9}
Result:
 3
Explanation:
 The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.
```
```
Example 2:

Input Format:
 N = 5, k = 2, arr[] = {4,2,1,3,6}
Result:
 5
Explanation:
 The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions {1, 6}. 
```

<br>

## Brute Force Approach 

### Algorithm
- [Watch it here](https://youtu.be/R_Mfw4ew-Vo?si=tk4b8Bg91x1Tck5u&t=414)
1. Sort the stalls array
2. For i in `range(max(arr)-min(arr))` we try to place cows with `1` to `arr[n-1]-arr[0]` spaces in between them.
3. If we are no longer able to place cows with i number of spaces between them, we stop

### Code 

```python
def aggressiveCows(stalls, k):
    n = len(stalls)
    limit = max(stalls)-min(stalls)
    stalls.sort()
    print(stalls)
    for i in range(min(stalls),max(stalls)+1):
        if not can_we_place(stalls,i,k):
            return i-1
    
    return limit

def can_we_place(arr,distance,no_of_cows):
    count_cows = 1
    last_cow_position = arr[0]

    for i in range(len(arr)):
        if arr[i]-last_cow_position >= distance:
            last_cow_position = arr[i]
            count_cows += 1
            if count_cows >= no_of_cows : 
                return True
        else:
            continue
    return False

if __name__ == "__main__":
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4
    ans = aggressiveCows(stalls, k)
    print("The maximum possible minimum distance between cows is:", ans)
```
- Time complexity : O(max-min) x O(n)
  - this is almost a quadratic (O(n<sup>2</sup>)) TC
- Space complexity : O(1)

<br>

## Optimal Approach 

- We can use Binary Search for this question

### Algorithm 

- [Watch it here](https://youtu.be/R_Mfw4ew-Vo?si=e--P6VqMnwzN3cBK&t=1139)
1. Binary Search the array. If the distance between the cows (mid) is possible, move the low up
2. If it is not possible, move the high down
3. By the rule of opposite polarity, the low will start from possible and end up at not possible and the high will start at not possible and end up at possible 
4. Hence high pointer will have our answer and we return that

### Code 

```python 
def aggressiveCows(stalls, no_of_cows):
    stalls.sort()
    n = len(stalls)
    low = 0
    high = stalls[n-1]-stalls[0]
    
    while low<=high:
        mid = (low+high)//2
        if can_we_place(stalls,mid,no_of_cows):
            # possible answer
            low = mid+1
        else:
            # not possible
            high = mid-1
    
    return high

def can_we_place(stalls,distance,no_of_cows):
    count=1
    last_cow_position = stalls[0]
    
    for i in range(len(stalls)):
        if stalls[i]-last_cow_position>=distance:
            last_cow_position = stalls[i]
            count+=1
            if count >= no_of_cows:
                return True
        else:
            continue
    return False

if __name__ == "__main__":
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4
    ans = aggressiveCows(stalls, k)
    print("The maximum possible minimum distance between cows is:", ans)
```
- **Time complexity : [ O(nlogn) ] + [ O(log<sub>2</sub>(max(arr)-min(arr))) x O(N) ]**
- **Space complexity : O(1)**

<br>

---
---