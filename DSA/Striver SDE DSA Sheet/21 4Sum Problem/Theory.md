# 4Sum Problem 

- Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    - 0 <= a, b, c, d < n
    - a, b, c, and d are distinct.
    - nums[a] + nums[b] + nums[c] + nums[d] == target
- You may return the answer in any order.

---

## Brute Force Approach 

- Just generate all teh 4 pairs using 4 loops 

### Algorithm

- [Watch it here](https://youtu.be/eD95WRfh81c?si=MmEjnUJGH9R44eb-&t=144)

### Code 

```python 
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        uniqueSet = set()

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        sum = nums[i]+nums[j]+nums[k]+nums[l]
                        
                        if sum == target:
                            quadruplets = (nums[i],nums[j],nums[k],nums[l])
                            uniqueSet.add(quadruplets)
        
        return [list(quadruplets) for quadruplets in uniqueSet]



if __name__ == "__main__":
    i = Solution()
    nums1,t1 = [1,0,-1,0,-2,2],0
    nums2,t2 = [2,2,2,2,2],8

    print(i.fourSum(nums1,t1))
    print(i.fourSum(nums2,t2))
```
- **Time Complexity : O(n<sup>4</sup>)**
- **Spacde Complexity : O(no. of quads)**

---

## Better Approach 

### Algorithm 

[Watch it here](https://youtu.be/eD95WRfh81c?si=5dR29FYcg8qFhtFq&t=376)

### Code 

```python
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        answerSet = set()

        for i in range(n):
            for j in range(i+1,n):
                hashmap = set()
                for k in range(j+1,n):
                    l = target - (nums[i] + nums[j] + nums[k])
                    
                    if l in hashmap:
                        quadruplets = [nums[i],nums[j],nums[k],l]
                        quadruplets.sort()
                        answerSet.add(tuple(quadruplets))
                    
                    hashmap.add(nums[k]) 
        
        return [list(quadruplets) for quadruplets in answerSet]

if __name__ == "__main__":
    i = Solution()
    nums1,t1 = [1,0,-1,0,-2,2],0
    nums2,t2 = [2,2,2,2,2],8

    print(i.fourSum(nums1,t1))
    print(i.fourSum(nums2,t2))
```
- **Time complexity : O(n<sup>3</sup>) + O(log(m))** (m is variable)
- Space complexity : O(n) + O(no. of quads) (internal hash + set)

---

## Optimal Approach 

- We still need to run 3 loops
- We just remove the extra data structures.

### Algorithm 

- sort the array
- [watch it here](https://youtu.be/eD95WRfh81c?si=7Zr0R64z5MOtC5kD&t=912)

### Code 

```python 
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        
        for i in range(n):
            if i != 0 and nums[i]==nums[i-1]: continue 
            else : 
                for j in range(i+1,n):
                    if j != i+1 and nums[j]==nums[j-1]: continue
                    else:
                        k = j+1
                        l = n-1
                        
                        while k<l:
                            sum = nums[i] + nums[j] + nums[k] + nums[l]
                            if sum == target:
                                quadruplets = [nums[i],nums[j],nums[k],nums[l]]
                                ans.append(quadruplets)
                                
                                k+=1
                                l-=1
                                while nums[k]==nums[k-1] and k<l : k+=1
                                while nums[l]==nums[l+1] and k<l : l-=1
                            elif sum < target:
                                k+=1
                            elif sum > target:
                                l-=1
        return ans
        
if __name__ == "__main__":
    i = Solution()
    nums1,t1 = [1,0,-1,0,-2,2],0
    nums2,t2 = [2,2,2,2,2],8

    print(i.fourSum(nums1,t1))
    print(i.fourSum(nums2,t2))
```
- **Time complexity : O(nlogn) + O(n<sup>3</sup>)**
- **Space Complexity : O(no. of quads)**    (for the ans list)