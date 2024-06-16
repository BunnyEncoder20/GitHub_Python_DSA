# Two Sum Problem 

---
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
- You may assume that each input would have exactly one solution, and you may not use the same element twice.
- You can return the answer in any order.

**Example 1:**
> Input: nums = [2,7,11,15], target = 9
> Output: [0,1]
> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**
> Input: nums = [3,2,4], target = 6
> Output: [1,2]

**Example 3:**
> Input: nums = [3,3], target = 6
> Output: [0,1]

- Can also ask you to just return true / false if such a pair exists.

---

## Brute Force Approach 

### Code 

```python 
def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    ans.append(i)
                    ans.append(j)
            if ans : break
                        
        return ans
```
- **Time Complexity : O(n<sup>2</sup>)**
- **Space Complexity : O(1)**

---

## Better/Optimal Approach 

- We can use hashing to improve the the time complexity to O(n)
- We can use a Dictionary Hashmap for this, storing number and it's index in it.
- Better Approach is the most optimal approach for variety 1 (in which we need to return the indexes)

### Code

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            require = target-nums[i]
            if require in hashmap:
                return [hashmap[require],i]
            else:
                hashmap[nums[i]] = i 
        


if __name__ == "__main__":
    nums1,t1 = [2,7,11,15],9
    nums2,t2 = [3,2,4],6
    nums3,t3 = [3,3],6

    i = Solution()
    print(i.twoSum(nums1,t1))
    print(i.twoSum(nums2,t2))
    print(i.twoSum(nums3,t3))
```
- **Time Complexity : O(n * logN)** (O(log n) for the map search)
- **Space Complexity : O(n)**

--- 

## Optimal Approach (Greedy Approach)

- Same TC as the better one, just doesn't use the map/dictionary DS
- **Only Applicable for the variety 2 (True/False return type) variant.**
- Because we sort the array and the original indices are lost

### Code 

```python 
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left,right = 0,n-1
        nums.sort()         

        while left<right:
            sum = nums[left]+nums[right]

            if sum == target : 
                return True
            elif sum < target :
                left+=1
            else:
                right-=1
        
        return False

if __name__ == "__main__":
    nums1,t1 = [2,7,11,15],9
    nums2,t2 = [3,2,4],6
    nums3,t3 = [3,3],6

    i = Solution()
    print(i.twoSum(nums1,t1))
    print(i.twoSum(nums2,t2))
    print(i.twoSum(nums3,t3))
```

- **Time Complexity : O(nlogn)+O(n)** (extra for sorting)
- **Space Complexity : O(1)**