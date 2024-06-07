# Majority Element 

- States that we need to find the element which occirs **more** than n/2 times 
- Eg:
```
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

---

## Brute Approach 

- Pick an element and linear search the entire array for the element. 
- Increamenet the count and if the count > (n/2) Then that is our answer 

<br>

- **Time Complexity : O(n<sup>2</sup>)**
- **Space Complexity : O(1)**

### Code 

```python
def majorityElement(nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j] : count+=1
            if count > (n//2) : 
                return nums[i]

        return -1
```

---

## Better Approach 

- We can optimize this problem by using hashing 
- We will use a dicitonary with elements being the keys and their frequence being the value.
- Once iteration over the array is over, we iterate over the Map.
- We return the key whose frequence is > n/2

<br>

- **Time Complexity : O(nlogn)+O(n)**
- **Space Complexity : O(n)** (worst case of all unique elements)

<br>

### Code 

```python 
from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums : 
            if num in hashmap:
                hashmap[num]+=1
            else : 
                hashmap[num]=1
        
        for key,val in hashmap.items():
            if val > len(nums)//2:
                return key
        
        return -1

if __name__ == "__main__":
    nums1 = [3,2,3]
    nums2 = [2,2,1,1,1,2,2]
    i = Solution()

    print(i.majorityElement(nums1))
    print(i.majorityElement(nums2))
```

---

## Optimal Approach (Moore's Voting Algorithm)

- Important to understand the initution and Thought process of algorithms. 
- **Time Complexity : O(n) + O(n)** (Note that the 2nd O(n) will not be there if there is always a majority element in the arrays)
- Space Complexity : O(1)


<br>

### Algorithm 

1. We take 2 Variables : 
    - element = not initialized 
    - count = 0
2. We start iterating over the array using a pointer. We assume that the number is our answer and assign it to element and make count as 1 
3. If the next element is the same as the previous, we increament the count. 
4. Else we decremenet the count by 1. 
5. If we reach zero, then we can assume that the inital element which we assigned is not majority element till that part of the array for sure (because the count reached zero). 
6. If we see that the count is zero, we take the current pointer number as the new element and make the count 1.
7. If at the end of the array, there is element, then we can say that if there is a majority element, then it'll be that element and no other num. 

<br>

Hence the Entire problems Algorithm can be summarized as : 
1. Apply Moore's Voting Algorithm 
2. Verify that the element we got is actually the majority element. We Do this by iterating over the array, counting the occurances of that element. 

<br>

### Code 

```python 
def majorityElement(nums: List[int]) -> int:
    n = len(nums)
    count = 0
    element = None

    for i in range(n):
        if count == 0 :
            element = nums[i]
            count = 1
        elif nums[i]==element :
            count+=1
        else:
            count-=1
    # After the above loop we will have some value in the element variable. 

    elementCounter = 0
    for i in range(n):
        if nums[i]==element:
            elementCounter+=1
    if elementCounter > n//2 :
        return element
    else : 
        return -1
```

---