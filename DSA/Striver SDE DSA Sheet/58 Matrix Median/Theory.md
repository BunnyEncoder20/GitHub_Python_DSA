# Median of Row Wise Sorted Matrix

- **Pre-requesites : Upper and Lower Bound (61 dir)**

<br>

- Given a row-wise sorted matrix of size MXN, where M is no. of rows and N is no. of columns, find the **median** (element right at the center if we convert the 2D matrix into a sorted array) in the given matrix.
- The rows of the Matrix are sorted. 
- Note: `MxN` is odd. When both n and m are odd, the product will always be odd

- Examples : 
Example 1:
```
Input Format:M = 3, N = 3, matrix[][] =

                                        1 4 9 
                                        2 5 6
                                        3 8 7
                    
Result: 5
Explanation:  If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. So, median = 5
```
```
Example 2:
Input Format:M = 3, N = 3, matrix[][] =

                                        1 3 8 
                                        2 3 4
                                        1 2 5
                    
Result: 3
Explanation:  If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 7 8. So, median = 3
```

<br>

## Brute Force Approach

### Algorithm

- [Watch it here](https://youtu.be/Q9wXgdxJq48?si=MsO0ap9L7W1xWxCT&t=116)
- Convert the matrix into a 1D array and sort it
- The element at [n*m//2] index will be the median.

### Code

```python
def median(matrix,m,n):
    oneD = []
    for row in range(m):
        for col in range(n):
            oneD.append(matrix[row][col])
    oneD.sort()
    return oneD[(m*n)//2]

if __name__=="__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [8, 9, 11, 12, 13],
        [21, 23, 25, 27, 29]
    ]
    m = len(matrix)
    n = len(matrix[0])
    ans = median(matrix, m, n)
    print("The median element is:", ans)
```
- Time complexity : O(nxm) + O(nxmlog(nxm))
- Space complexity : O(nxm)

<br>

## Optimized Algorithm

- We need to reduce the time complexity < nxm i.e; skip some portions. 
- We need to implement Binary Search into the problem

### Algorithm 

- The key thing to observe / remember here is : 
```
no. of elements (before/left of/less than equal) to median > n*m//2 always
```
- Which basically implies 
```
[no. of elements <= median] > (n*m)//2
```
- [Watch it here](https://youtu.be/Q9wXgdxJq48?si=L0D9419km7dTbVEK&t=292)
- we need to get the first occurance of element which has [elements<=it] > (n*m)//2
- Basically we have to upper bound the number which has elements lesser than equal to itself array with (n*m)//2

### Code 

```python
def median(matrix,m,n):
    low = float('inf')
    high = float('-inf')

    # Assign low and high values 
    # By checking the first and last col elements of the matrix
    # cuase the rows are sorted, the lowest values will be in col[0] and highest values of the rows will be in col[n-1]
    for i in range(m):
        low = min(low,matrix[i][0])
        high = max(high,matrix[i][n-1])
    
    # Our required number : 
    req = (n*m)//2
    
    # Binary Search
    while low<=high:
        mid = (low+high)//2
        elements_less_than_equal = BlackBox(matrix,n,m,mid)
        if elements_less_than_equal <= req:
            low = mid+1
        else:
            high = mid-1
    return low

def BlackBox(matrix,n,m,mid):
    '''
    returns the number of elements in the matrix <= mid
    '''
    count=0
    # go row wise and BS the row for upper bound of mid
    # Upper bound will retunr the index of the number just greator than mid
    # This giving is the exact count of elements <= mid
    for i in range(m):
        count+=upperBound(matrix[i],n,mid)
    return count

def upperBound(arr,n,x):
    low = 0
    high = n-1
    ans = n

    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            ans = mid       # maybe an answer 
            high=mid-1
        else:               # looking for a smaller index on the left 
            low = mid+1
    return ans

if __name__=="__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [8, 9, 11, 12, 13],
        [21, 23, 25, 27, 29]
    ]
    m = len(matrix)
    n = len(matrix[0])
    ans = median(matrix, m, n)
    print("The median element is:", ans)
```
- Time complexity : O(log<sub>2</sub>(10<sup>9</sup>) x nlog<sub>2</sub>m)
    - ATQ, the smallest number can be 1 and the largest number in the matrix can be 10<sup>9</sup>
    - O(log<sub>2</sub>(10<sup>9</sup>)) for the Binary Search
    - O(n) for traversingn the rows and sending it to Upper bound func
    - O(log<sub>2</sub>m) for the Upper bound
- Space complexity : O(1)