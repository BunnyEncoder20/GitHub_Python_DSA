# Grid Unique Paths

- There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either **down or right** at any point in time.
- Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

<br>

# Brute Force Approach 

- Brute Force Approach is a recursive approach. 
- **Time Complexity : O(2<sup>n</sup>) (exponential)** (because we are exploring all the possible paths)
- **Space Complexity : O(2<sup>n</sup>)** (because we are using stack space.)

<br>

### Algorithm

- Recursively move in 2 directions, right and down.
- Base case will be when 
    - i == m
    - j == n
- If we reach the target coord, we return 1 otherwise 0
- In the ened we will have our count of paths.

<br>

### Code 

```python 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i,j=0,0
        return self.countPaths(i,j,m,n)
    
    def countPaths(self,i,j,m,n):
        # reached the destination
        if i==n-1 and j==m-1 : return 1

        # reached outside the matrix 
        if i>=n or j>=m : return 0

        # remaining cases down+right
        return self.countPaths(i+1,j,m,n) + self.countPaths(i,j+1,m,n)

if __name__ == "__main__":
    i = Solution()
    m1,n1 = 3,7
    m2,n2 = 3,2

    print(i.uniquePaths(m1,n1))
    print(i.uniquePaths(m2,n2))
```

---

## Better Approach (Dynamic Programming Solution)

- We can better the complexity by converting the recursive code into a dynamic programming code 
- We know that for each recursive step the state can be [i][j] which at max can have the value [m][n]. 
- And the total number of such states possible are mxn
- Hence we make a hash table of mxn, initialized to -1.
- If we visit a state for the first time and it returns a value of 1, we can store that state into our Hash table.
- When some other branch of the recursion, tries to take the same state again, we can simple grab it's value from the hash table without performing the recursion. 
- This is called **Dynamic Programming** in which we retrieve previously computed values without actually performing the computation in current step.

<br>

- **Time complexity : O(nxm)**
- **Space Complexity : O(mxn)**

### Code : 

```python 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        hashtable = [[-1 for i in range(n)] for j in range(m)]
        i,j=0,0
        return self.countPaths(i,j,m,n,hashtable)
    
    def countPaths(self,i,j,m,n,hashtable):
        if i==m-1 and j==n-1: return 1 
        if i>=m or j>=n : return 0 

        # If the value of that state there in the hashtable, return that value else calculate it recursively
        if hashtable[i][j]!=-1 : 
            return hashtable[i][j]
        else : 
            hashtable[i][j] = self.countPaths(i+1,j,m,n,hashtable) + self.countPaths(i,j+1,m,n,hashtable)
            return hashtable[i][j]
    
if __name__ == "__main__":
    i = Solution()
    m1,n1 = 3,7
    m2,n2 = 23,12

    print(i.uniquePaths(m1,n1))
    print(i.uniquePaths(m2,n2))
```

---

## Optimal Approach (Combination)

### Observations 

- Consider the following matrix : 
```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```
- We observe that the number of steps to reach the destination are always 3.
- We also observe that there is a fixed number of right moves and down moves we need to make in order to get to the destination : 
    - we need n-1 no. of right moves (cols-1) 
    - we need m-1 no. of down moves  (rows-1)
- Hence the total number of steps which we need to take in order to get to the destination is given by : 
```
total steps = m + n - 2
```
- Hence we know that we have m+n-2 places need to fill with (m-1) down moves or (n-1) right moves.
- Hence we can get our answer from any one of the following combinations : 
    - <sup>(m+n-2)</sup>C<sub>m-1</sub>
    - <sup>(m+n-2)</sup>C<sub>n-1</sub>
- Remember the shortcut for calculating the Combiantion : 
    - <sup>10</sup>C<sub>3</sub> = (10x9x8) / (3x2x1)

<br>

- **Time Complexity : O(m-1) or O(n-1)**
- **Space Complexity : O(1)**

<br>

### Code 

```python 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n = m+n-2
        r = min(m-1,n-1)     # use the smaller of m-1 or n-1 to reduce the number of calculations
        ans = 1

        for i in range(1,r+1):
            ans = (ans * ((n-r)+i)) // i
            # Be careful of this line 
        
        return ans 

if __name__ == "__main__":
    i = Solution()
    m1,n1 = 3,7
    m2,n2 = 23,12

    print(i.uniquePaths(m1,n1))
    print(i.uniquePaths(m2,n2))
```