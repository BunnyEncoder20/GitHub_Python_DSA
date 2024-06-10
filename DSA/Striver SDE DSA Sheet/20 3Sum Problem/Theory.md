# 3Sum Problem

- Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
    - i != j, i != k, and j != k 
    - nums[i] + nums[j] + nums[k] == 0.
- Notice that the solution set must not contain duplicate triplets.

---

## Brutre Force Approach 

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
- **Time Complexity : O(n<sup>3</sup>)**
- **Space Complexity : 2*O(no. of triplets)**

---

## Better Approach

- We try to make the complexity better by removing the 3rd loop.
- We will use hashing for this (because it takes log or constant time)

### Algorithm 
- [watch it here](https://youtu.be/DhFh8Kw7ymk?si=KTDmXutZJotpehuu&t=745)


### Code 

```python 

```

