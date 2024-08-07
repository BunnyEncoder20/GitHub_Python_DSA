# 3Sum Problem

- Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
    - i != j, i != k, and j != k 
    - nums[i] + nums[j] + nums[k] == 0.
- Notice that the solution set must not contain duplicate triplets.

---

## Brute Force Approach 

- Try out all of the triplets using 3 loops

### Algorithm 

- [watch it here](https://youtu.be/DhFh8Kw7ymk?si=Sy8BEiCnH3LHb70N&t=290)

### Code 

```python 
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answerSet = set()

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        answerSet.add(tuple(temp))

        return [list(triplets) for triplets in answerSet]

if __name__ == "__main__":
    i = Solution()
    numsList = [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]]
    
    for nums in numsList : 
        print(i.threeSum(nums))
```
- **Time Complexity : O(n<sup>3</sup>) + O(log(no. of triplets))** (because we are using set DS)
- **Space Complexity : 2*O(no. of triplets)** (answerSet + temp)

---

## Better Approach

- We try to make the complexity better by removing the 3rd loop.
- We will use hashing for this (because it takes log or constant time)

### Algorithm 
- [watch it here](https://youtu.be/DhFh8Kw7ymk?si=KTDmXutZJotpehuu&t=745)


### Code 

```python 
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ansSet = set()
        
        for i in range(n):
            hashset = set()
            
            for j in range(i+1,n):
                k = 0 - (nums[i]+nums[j])
            
                if k in hashset : 
                    temp = [nums[i],nums[j],k]
                    temp.sort()
                    ansSet.add(tuple(temp))

                hashset.add(nums[j])
        
        return [list(triplets) for triplets in ansSet]


if __name__ == "__main__":
    i = Solution()
    numsList = [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]]
    
    for nums in numsList : 
        print(i.threeSum(nums))
```

- **Time complexity : O(n<sup>2</sup>) * O(log m) = O(n<sup>2</sup>)** (approx)
- **Space complexity : O(n) + O(no. of triplets)** (hashmap + answer set)

---

## Optimal Approach

### Algorithm
- [Watch it here](https://youtu.be/DhFh8Kw7ymk?si=5rqG_Z7ye-bycuul&t=1340)
- sort the array 
- fix i, move j++ and k-- and store the triplets 
  
### Code

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue 
            else:
                j = i+1
                k = n-1
                
                while j<k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        ans.append([nums[i],nums[j],nums[k]])
                        j+=1
                        k-=1
                        
                        while nums[j]==nums[j-1] and j<k : j+=1
                        while nums[k]==nums[k+1] and j<k : k-=1

                    elif sum<0:
                        j+=1
                    elif sum>0:
                        k-=1 
        
        return ans

if __name__ == "__main__":
    i = Solution()
    numsList = [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]]
    
    for nums in numsList : 
        print(i.threeSum(nums))
```
- **Time Complexity : O(nlogn) + O(n<sup>2</sup>)**
- **Space Complexity : O(no. of triplets)**
