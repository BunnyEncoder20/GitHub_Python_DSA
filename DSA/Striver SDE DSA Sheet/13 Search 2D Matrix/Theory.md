# Search in a 2D Matrix 

- Given a sorted mat of mxn, return True if Target is present in the Matrix else return False.

---

## Brute Force Solution 

- Siimply traverse the matrix and find the target.
- **Time Complexity : O(nxm)**
- **Space Complexity : O(1)**

## Code 

```python 
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target : return True
        
        return False
```

---

## Better Solution

- We can take advantage of the fact that the matrix is sorted. 
- Hence we can implement Binary search on a specific row to find our target.
- **Time Complexity: O(m) + O(log<sub>2</sub>n)** (where `m` is no. of rows and `n` is no. of cols)
- **Space Complexity: O(1)**

### Binary Serach 

- Searching algorithm for searching in a limited space of sorted arrays. 
- The array has to be sorted and unique. 
- **Time Complexity : O(log<sub>2</sub>n)**

<br>

- Iterative Method 

```python 
def binarySearch(arr,n,target):
    low = 0
    high = n-1

    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target :
            return True 
        elif target < arr[mid] :
            high = mid-1
        else : 
            low = mid+1
    
    return False
```

<br>

- Recursive Implementation 

```python 
def recursiveBinarySearch(arr,low,high,target):

    # base case 
    if low>high : return False

    mid = (low+high)//2
    if arr[mid] == target:
        return True
    elif arr[mid] < target :
        return recursiveBinarySearch(arr,mid+1,high,target)
    else : 
        return recursiveBinarySearch(arr,low,mid-1,target)
```

<br>

### Algorithm

1. Go row by row and check if the Target lies between row[0] and row[n-1]
2. If the element doesn't lie between the two, then we will not check that row. 
3. Only when the Target lies between the first and last element will be saerch that row. 
4. Because the row (1D array) is sorted, we can implement binary search on the row to find our element. 

- **Time Complexity : O(m) + O(log<sub>2</sub>n)**
- **SPace Complexity : O(1)**

<br>

### Code 

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = n-1

        for i in range(m):
            if matrix[i][0] <= target and target <= matrix[i][n-1] :
                return self.binarySearch(matrix[i],low,high,target)
    
    def binarySearch(self,arr,low,high,target):

        # base case 
        if low>high : return False

        # remaining case 
        mid = (low+high)//2

        if arr[mid] == target :
            return True 
        elif arr[mid] < target : 
            return self.binarySearch(arr,mid+1,high,target)
        else : 
            return self.binarySearch(arr,low,mid-1,target)
```

---

### Optimal Solution 

- We can further optimize the solution by Treating (not converting) the 1D matrix as a 2D matrix.
- If we treat it as a 1D sorte array, when we can simply apply binary search and get a better time complexity. 
- We just need a mapping from an index into it's 2D coordinate 

- **Time Complexity : O(log<sub>2</sub>nxm)**
- **Space Complexity : O(1)**

### Algorithm 

1. If we have a index then the formula to convert that into it's 2D coordinate is :
    - **rows = index / no. of cols**
    - **cols = index % no. of cols**
2. Now we take 
    - low = 0
    - high = (mxn)-1
3. Using bianry search algo : 

```python
while low<=high:
    mid = (low+high)//2
    row = mid/len(matrix[0])
    col = mid%len(matrix[0])

    if matrix[row][col] == target : 
        return True
    elif matrix[row][col] < target : 
        low = mid+1
    else : 
        high = mid-1
return False 
```
<br>

### Code 

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m*n-1

        while low <= high : 
            mid = (low+high)//2
            row = mid//n
            col = mid%n

            if matrix[row][col] == target : 
                return True 
            elif matrix[row][col] < target : 
                low = mid+1
            else : 
                high = mid-1
        
        return False 
        

if __name__ == "__main__":
    ins = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    target2 = 13
    print(ins.searchMatrix(matrix,target1))
    print(ins.searchMatrix(matrix,target2))
```
