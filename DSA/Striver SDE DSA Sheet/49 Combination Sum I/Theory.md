# Combination Sum - I 

Given an array of distinct integers and a target, you have to return the list of all unique combinations where the chosen numbers sum to target. You may return the combinations in any order.

```
Example 1:
Input: array = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Explanation: 
2 and 3 are candidates, and 2 + 2 + 3 = 7. 
Note that 2 can be used multiple times. 
7 is a candidate, and 7 = 7.
These are the only two combinations.


Example 2:
Input: array = [2], target = 1
Output: []
Explaination: No combination is possible.
```

<br>

## The Recursive Approach 

- Thinking recursively : Whenever there is a problem in which we have to pick elements from an array to form a combination, always think about the picked-not-picked algorithm.

## Algorithm 

![alt text](<pasted image 0.png>)

- We do the pick-not-pick algo and recursively call the function to generate all the possible combinations 
- Since we can pick same element multiple times, we do not move the index when we pick a index, we just reduce the target with that nums[index], i.e; `func(index,target-nums[index],ds)`
- When we don't pick an element, we increase the index, target and ds remain the same


### Code 

```python 
from typing import List 

class Solution:
    def combinationSum(self,candidates:List[int],target:int)->List[List[int]]:
        n = len(candidates)
        answer = []
        ds = []
        
        def combinationHelper(index,target):
            # base cases
            if index==n:
                if target==0 : answer.append(ds[:])
                return
            
            # remaining cases
            # we can only take the index if it is less than target
            if candidates[index]<=target:
                ds.append(candidates[index])
                combinationHelper(index,target-candidates[index])
                ds.pop()
            # else we just move onto the next element
            combinationHelper(index+1,target)
        
        combinationHelper(0,target)
        return answer

if __name__ == "__main__":
    obj = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    ans = obj.combinationSum(candidates, target)
    print("The original candidates are :")
    for num in candidates:
        print(num, end=' ')
    print()
    print("Combinations are: ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()
```
- **Time complexity : O(2<sup>n</sup> * k)**
  - 2<sup>n</sup> for the logarithm recursion 
  - k = avg length of subLists