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

### Algorithm 
- [Watch it here](https://youtu.be/oO5uLE7EUlM?si=o-xfsL7dSkK5txM4&t=320)
- sort the array
- keep a last min, if current element-1 is the last min, counter+1
- else restart counter and seq

### Code

```python 
from typing import List 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        longest = 0
        streak = 0
        last_smaller = float('-inf')

        for i in range(n):
            if nums[i]-1 == last_smaller : 
                streak+=1
                last_smaller = nums[i]
            elif nums[i]-1 != last_smaller : 
                streak = 0
                last_smaller = nums[i]
            else : # for nums[i]==last_smaller, we do not do anything, just incraese the counter
                continue
            
            longest = max(longest,streak)

if __name__ == "__main__":
    numsList = [[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]]
    i = Solution()
    
    for nums in numsList :
        print(i.longestConsecutive(nums))
```
- **Time Complexity : O(nlog(n)) + O(n)** (for the sorting + loop)
- **Space compleixty : O(1)**
- Distorts the array so can ask you to optimize by not doing that or removing the nlog(n) complexity.

---

## Optimal Approach 

### Algorithm 

- [Watch it here](https://youtu.be/oO5uLE7EUlM?si=qyRJ8-sPxsZ6ydop&t=775)
- put all elements into a **set DS**
- iterate over them one by one.
- if it's prev is presnet in the DS, don't check further cause it not the start of a seq
- if it's prev not preset, it is start and check of it's previous values till you can't get one.
- update the longest count

### Code 

```python 
from typing import List 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 : return 0

        longest = 0 
        elements = set()    # takes O(1) avg lookup time 

        for i in range(n):
            elements.add(nums[i])
        
        for num in elements:
            if num-1 in elements : 
                continue
            else :
                streak=1
                x = num 
                while x+1 in elements : 
                    x+=1
                    streak+=1
                longest = max(longest,streak)

        return longest


if __name__ == "__main__":
    numsList = [[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]]
    i = Solution()
    
    for nums in numsList :
        print(i.longestConsecutive(nums))
```
- Sets lookup takes on avg O(1) times. In case of collisions (very rare case) it will take O(n)
- **Time complexity : O(n) + O(1) + O(2n) = O(3n)** (2n for while loop) (Also assuming that set gives O(1) look up)
- **Space complexity : O(n)**   (for the set DS)