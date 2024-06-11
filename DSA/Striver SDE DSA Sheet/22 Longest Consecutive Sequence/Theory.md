# Longest Consecutive Sequence

- Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
- You must write an algorithm that runs in O(n) time.
- Examples : 

**Example 1:**
> Input: nums = [100,4,200,1,3,2]
> Output: 4
> Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

**Example 2:**
> Input: nums = [0,3,7,2,5,8,4,6,0,1]
> Output: 9

---

## Brute Force Approach 

- pick and element 
- check if it's next number in the array.
- If yes, increase counter and check for it's next number 
- Else reset counter and move to next element in array

### Algorithm

- [Watch it here](https://youtu.be/oO5uLE7EUlM?si=TRtt-dBdTubP0CP3&t=124)

### Code 

```python 
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        n = len(nums)
        
        for i in range(n):
            num = nums[i]
            counter = 1
            
            while num+1 in nums:
                num+=1
                counter+=1
            
            longest = max(longest,counter)
        
        return longest
        

if __name__ == "__main__":
    numsList = [[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]]
    i = Solution()
    
    for nums in numsList :
        print(i.longestConsecutive(nums))
```
- **Time complexity : O(n<sup>2</sup>)**
- **Space complexity : O(1)**

---

## Better Approach