# Maximum and Minimum Element in an Array

## Q) Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons. [link](https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/)

### Examples:
```
Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
              Maximum element is: 9

Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
              Maximum element is: 35
```
### Approach 1 : Using sorting 

```python
def min_max(l):
    l.sort()
    print(f"The minimum element is {l[0]}")
    print(f"The maximum element is {l[-1]}")

if __name__ == '__main__':
    l = [22, 14, 8, 17, 35, 3]
    min_max(l) 
```
- Output
```
Minimum element is 3   
Maximum element is = 35
```
- **NOTE:** the default `.sort()` method for python list uses an implementation of `Timsort`,which is a hybrid sorting algorithm derived from `merge sort` and `insertion sort`.
- Time complexity of Timsort is `O(n log(n))` in worse case.
- Hence the Time complexity for the above implementation is **`O(nlog(n))`**

### Approach 2 : Linear Search 

```python 
def min_max(l):
    if len(l) == 0:
        return f"There is only 1 value so Min = Max= {l[0]}"
    elif l[0]<l[1]:
        min = l[0]
        max = l[1]
    else : 
        min = l[1]
        max = l[0]
        
    # linear searching 
    for num in l[2:] :
        if num < min :
            min = num
        if num > max : 
            max = num
    
    return f"Minimum element is {min} \nMaximum element is = {max}"
        

if __name__ == '__main__':
    l = [22, 14, 8, 17, 35, 3]
    print(min_max(l))
    
```
Output :
```
Minimum element is 3   
Maximum element is = 35
```
- Time Complexity : `O(n)`
- Space Complexity : `O(1)`

### Approach 3 : Tournament Method:

>- The idea is to divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.

- This is a recursive method, so I'll not even bother with trash like this 
- It's time complexity is also high,
- It's space complexity is also high
- It's number of comparisons is lowest (not by a lot and that also not clearly mentioned by it is lower or how is it lower)

### Approach 4 : Comparing in Pairs 

> The idea is that when n is odd then initialize min and max as the first element. If n is even then initialize min and max as minimum and maximum of the first two elements respectively. For the rest of the elements, pick them in pairs and compare their maximum and minimum with max and min respectively. 

- Time Complexity : `O(n)`
- Space Complexity : `O(1)`
- Number of comparisons : 
  - Odd : 3*(n-1)/2
  - Even : 1 for initial and 3(n-2)/2 comparisons for the rest of elements
- Note that **Approach 4** is best for general cases.

```python 
def minmax(list):
    
    if len(list)%2 == 0 :       # if list has even no. of elements
        if list[0] < list[1] :
            mini = list[0]
            maxi = list[1]
        else :
            mini = list[1]
            maxi = list[0]
        i = 2   
    else :                      # list has odd number of elements 
        mini = maxi = list[0]
        i = 2 
    
    while i < len(list)-1 :
        if list[i] < list[i+1] :        # compare the elements in pairs 
            mini = min(mini,list[i])
            maxi = max(maxi,list[i+1])
        else : 
            mini = min(mini, list[i+1])
            maxi = max(maxi, list[i])
        i+=2                            # updating i to next pair
    
    return mini,maxi

if __name__ == '__main__':
    arr = [1000, 11, 445, 1, 330, 3000]
    mini,maxi = minmax(arr)
    print(f"Minimum element is {mini}\n Maximum element is {maxi}")
```