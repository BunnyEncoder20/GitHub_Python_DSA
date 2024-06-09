# Majority Elements n/3 Times 

- Return all the majority elements of an array which appear more than n/3 times 
- Eg: 
```
> Input  : [1,1,1,3,3,2,2,2]
> Output : [1,2]    (8//2 = 2)
```
- **Note:** That at max, the number of elements that will be more than floor of n/3 will be 2 elements only. 
- Take the above example, we need majority element to appear at least 3 times. 
- Hence if the answer had 3 elements then the size of the array would have to be at least 3+3+3 = 9. 
- Hence we can definitely say that there will be only 2 elements which can appear more than n/3 times.

---

## Brute Force Approach  

- Linear search the array for each element and return element(s) which appeared more than n/3 times.

### Algorithm 

1. Start with a pointer at starting. Iterate over the array.
2. If element is not in the ans array, Start another pointer to count it's total occurrences in the array. 
3. If it's count is more than n/3 times, append it into the answer array. 
4. Check to see if the number of elements in ans array is not more than than 2. If it is already at 2, return the answer array, else continue. 

<br>

- **Time Complexity : O(n<sup>2</sup>)**
- **Space Complexity : O(1)**

<br>

### Code 

```python
def majorityElement(nums: List[int]) -> List[int]:
    ans = []
    n = len(nums)
    
    for i in range(n):
        if len(ans)==0 or nums[i] not in ans:
            count=0
            for j in range(n):
                if nums[i]==nums[j]:
                    count+=1
            if count > n//3:
                ans.append(nums[i])

        if len(ans)==2: break
    
    return ans
```

---

## Better Approach 

- We can improve on the O(n<sup>2</sup>) time complexity by using **Hashmap**
- **Time Complexity : O(n)**
- **Space Complexity : O(n)**

<br>

### Algorithm 

- Declare an empty hashmap dict[element:count]
- Iterate over the array and update the hashmap.
- After this iterate over the hashmap and return the elements which have count > n/3 times. 

**But** we can further optimize by removing the step in which we need to iterate4 over the hashmap.

- While updating the count in the hashmap itself, we check the count, and if it becomes (n//3)+1 then we add it directly into our ans array. 
- This way we only iterate over the array once.

<br>

### Code 

```python
def majorityElement(nums: List[int]) -> List[int]:
    n = len(nums)
    hashmap = {}
    ans = []
    atleast = (n//3) + 1

    for i in range(n):

        if nums[i] not in hashmap:
            hashmap[nums[i]] = 1
        else : 
            hashmap[nums[i]] += 1

        if hashmap[nums[i]] == atleast:
            ans.append(nums[i])
        
        if len(ans) == 2 : break 
    
    return ans
```
<br>

---

## Optimal Approach 

- We will use a modified version of Moore's Voting algorithm.
- **Time Complexity : O(n)+O(n)+O(1) = O(2n)**
- **Space Complexity : O(1)**

### Algorithm 

1. Take variables : 
    - counter1 = 0
    - counter2 = 0
    - element1 = None
    - element2 = None
2. We iterate from 0 to n
3. If counter1 = 0 , we assign nums[i] into element1 (make sure it is not element2)
4. Elif counter2 = 0, we assign nums[i] into element2 (make suer it is not element1)
5. Elif nums[i] == element1, counter1+=1 
6. Elif nums[i] == element2, counter2+=1 
7. Else counter1-=1 and counter2-=1
8. After iterating over the array, we can manually check for whether element 1 and element 2 are majority elements or not. 

<br>

### Code 

```python
from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter1,counter2 = 0,0
        element1,element2 = None,None 
        n = len(nums)

        for i in range(n):
            if counter1==0 and nums[i] != element2:
                element1 = nums[i]
                counter1 = 1
            elif counter2==0 and nums[i] != element1:
                element2 = nums[i]
                counter2 = 1
            elif nums[i]==element1 : counter1+=1
            elif nums[i]==element2 : counter2+=1
            else:
                counter1-=1
                counter2-=1
        
        # After the above loop we will have some number in element1 and element2, but cannot say for sure they are the majority elements (in case there might not be any majority elements)
        # Hence we need to verify
        count1,count2=0,0
        ans = []
        for num in nums:
            if num == element1 : count1+=1
            if num == element2 : count2+=1 
        if count1>n//3 : ans.append(element1)
        if count2>n//3 : ans.append(element2)
        
        ans.sort() 
        return ans


if __name__ == "__main__":
    listNums = [[3,2,3],[1],[1,2]]
    i = Solution()
    for num in listNums:
        print(i.majorityElement(num))
```
<br>
