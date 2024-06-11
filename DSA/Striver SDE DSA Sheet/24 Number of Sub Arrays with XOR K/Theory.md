# Number of Sub Arrays with XOR K

- Given an array of integers A and an integer B.
- Find the total number of subarrays having bitwise XOR of all elements equals to B.
- Examples : 

**Input 1:**
> A = [4, 2, 2, 6, 4]
> B = 6

**Output 1:**
> 4

**Input 2:**
> A = [5, 6, 7, 8, 9]
> B = 5

**Output 2:**
> 2

<br>

## Brute Force Approach 

### Algorithm
- [Watch it here](https://youtu.be/eZr-6p0B7ME?si=0gZ08v9Yh5s2ipGb&t=189)
- Generate all the sub arrays 
- calculate the xor, update the counter 

### Code 

```python 
class Solution:
    def solve(self, nums, target):
        n = len(nums)
        counter = 0

        for i in range(n):
            for j in range(i,n):
                xor = 0
                for k in range(i,j+1):
                    xor = xor^nums[k]
                if xor==target :
                    counter+=1
        return counter

if __name__ == "__main__":
    A1,A2 = [4, 2, 2, 6, 4],[5, 6, 7, 8, 9]
    B1,B2 = 6,5

    i = Solution()
    print(i.solve(A1,B1))
    print(i.solve(A2,B2))
```
- **Time complexity : O(n<sup>3</sup>)**
- **Space complexity : O(1)**

<br>

## Better Approach 

- We observe that we do not need the k loop to calculate the xor of all the elements

### Algorithm 
- [Watch it here](https://youtu.be/eZr-6p0B7ME?si=osA_XqXSREZuKpCv&t=372)

### Code 

```python 
class Solution:
    def solve(self, nums, target):
        n = len(nums)
        counter = 0

        for i in range(n):
            xor = 0
            for j in range(i,n):
                xor = xor ^ nums[j]    
                if xor==target :
                    counter+=1
        return counter

if __name__ == "__main__":
    A1,A2 = [4, 2, 2, 6, 4],[5, 6, 7, 8, 9]
    B1,B2 = 6,5

    i = Solution()
    print(i.solve(A1,B1))
    print(i.solve(A2,B2))
```
- **Time complexity : O(n<sup>2</sup>)**
- **Space complexity  : O(1)**

<br>

## Optimal Approach 

### Algorithm

- [Watch it here](https://youtu.be/eZr-6p0B7ME?si=ScKj86uhjzPSFZxY&t=490)

### Code 

```python
from collections import defaultdict

class Solution:
    def solve(self, nums, target):
        n = len(nums)
        counter = 0
        xor = 0
        hashmap = defaultdict(int) # defaultdict used because if the key is not present it'll return 0 by default
        hashmap[0]=1    # setting the first value

        for i in range(n):
            xor = xor ^ nums[i]
            required = xor^target

            counter += hashmap[required]  # if element in hashmap will return count of that else 0
            hashmap[xor]+=1

        return counter

if __name__ == "__main__":
    A1,A2 = [4, 2, 2, 6, 4],[5, 6, 7, 8, 9]
    B1,B2 = 6,5

    i = Solution()
    print(i.solve(A1,B1))
    print(i.solve(A2,B2))

```
- **Time complexity : O(n) or O(n) x O(log(n))**  (Or part depending on the maps complexity)
- **Space complexity : O(n)** 