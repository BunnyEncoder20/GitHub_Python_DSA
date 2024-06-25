# Subset Sum II - Print all Unique subsets

- Given an array of integers that may contain duplicates the task is to return all possible subsets. Return only unique subsets and they can be in any order.


<br>

## Brute Force Approach 

### Algorithm 

- We use the same recursive method of picking and not picking an element
- Then we will feed each of the List states (subsets) into a set to avoid duplicates 
- Finally we will convert the set elements into a list and return them.


### Code 

```python
from typing import List

class Solution:
    def subsetsWithDup(self,nums:List[int])->List[List[int]]:
        n = len(nums)
        result = set()

        def subsetsHelper(index,current):
            if index==n:
                current.sort()
                result.add(tuple(current))
                return 
            
            # one where we pick the number 
            current.append(nums[index])
            subsetsHelper(index+1,current)

            # one where we do not pick the number
            current.pop()
            subsetsHelper(index+1,current)
        
        subsetsHelper(0,[])
        answer = []
        for element in result:
            answer.append(list(element))
        answer.sort()
        return answer


if __name__ == "__main__":
    nums = [1, 2, 2]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print("[ ", end="")
    for i in range(len(ans)):
        print("[ ", end="")
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print("]", end="")
    print(" ]", end="")
```
- **Time complexity : O( 2^n * (k log (x) ))** 
  - k is avg length of each combination, 
  - into a set of size x
- **Space complexity : O(2<sup>n</sup> * k)**

<br>

## Optimal Approach 

- We get rid of the extra klog(x) time by optimzing the recursive calls

### Algorithm 

- [Watch it here](https://youtu.be/RIn3gOkbhQE?si=ytMDR65CiTotK9Pa&t=276)
- Use a `index` and `DS` to recursively generate all the combinations 
- We check if it's a duplicate (by checking with theh previous entry to DS, also do not check for duplicates when it's the first index of call) , we skip the duplicates and go to the unique ones
- Once a unique number is found, we add it into our DS and call the next recursion with index+1.
- This way we generate all the subsets and avoid the calls which generate the duplicates altogether.

### Code 

```python
from typing import List 

class Solution :
    def subsetsWithDup(self,nums:List[int])->List[List[int]]:
        n = len(nums)
        ds = []
        answer = []
        
        # we need the duplicates side by side 
        nums.sort()
        
        def subsetHelper(index:int)->None:
            answer.append(ds[:])

            for i in range(index,n):
                if i>index and nums[i]==nums[i-1]: continue
                ds.append(nums[i])
                subsetHelper(i+1)
                ds.pop()
        
        subsetHelper(0)
        return answer
        
    
if __name__ == "__main__":
    nums = [1, 2, 2, 2, 3, 3]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print("[ ", end="")
    for i in range(len(ans)):
        print("[ ", end="")
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print("]", end="")
    print(" ]", end="")
```
- **Time complexity : O(2<sup>n</sup> * n)**
  - `2<sup>n</sup>` for the recursive calls
  - `n` for inserting the result combinations into the answer list
- **Space complexity : O(2<sup>n</sup> * k)**
  - No. of subsets = `2<sup>n</sup>`
  - Average length of subset = `k`
- **Auxilary Space Complexity : O(n)**
  - Depth of recursion will go down `n` levels