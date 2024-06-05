# Finding Duplicate in a Array of N+1 Intergers

- Given an array of integers nums containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.
- There is only one repeated number in nums, return this repeated number.
- You must solve the problem without modifying the array nums and uses only constant extra space.

--- 

## Brute Force Solution 

### Algorithm 

- Sort the array. This will bring the duplicate elements side by side 
- Now by simple iteration over the loop, we can find the duplicate element.
- **Time Complexity : O(nlogn)**
- **Space Complexity : O(1)**
- However this approach distorts the original array. 

### Code 

```python
def findDuplicate(nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                dup = nums[i]
                break
        
        return dup
```

---

## Better Solution 

- We can better the naive approach by using Hashing
- **Time Complexity : O(n)**
- **Space Complexity : O(n)**
- By this approach we improve on the Time complexity but we are still using some extra space.

### Algorithm 

1. We create a frequence (hash) array of size of our original array, initalized to 0
2. As we iterate over the array, we can update the frequence of the elements one by one. 
3. When we encounter an element whose frequence is already 1, we can know that this is a duplicate element.

### Code 

```python 
def findDuplicate(nums: List[int]) -> int:
        freq_arr = [0]*len(nums)

        for num in nums:
            if freq_arr[num] == 1:
                return num 
            else:
                freq_arr[num] = 1
```

---

## Optimal Solution 

- This algorithm uses the LinkedList Cycle Method
- **Time Complexity : O(n)**
- **Space Complexity : O(1)**


### Algorithm 

1. We take 2 pointers : 
    - slow : moves 1 step at a time (tortose)
    - fast : moves 2 steps at a time (hare)
2. LinkedList Cycle methods works by pointer moving in the following manner:
Consider the following array : [2,5,9,6,9,3,8,9,7,1]
    - Starting at zero, 
    - the element at 0 is 2 , hence next index will be 2 
    - the element at 2 is 9 , hence next index will be 9
    - the element at 9 is 1 , hence next index will be 1
    - and so on...
3. The slow and fast pointers move in this manner, but at their different speeds (steps). 
4. When the two pointers collide, we reset the fast pointer  to the starting element and make it into another slow pointer. Now both pointers move by one step.
5. The next time the pointers collide will be out duplicate element. 

### Code 

```python 
def findDuplicate(nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True : 
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow==fast : break
        
        fast = nums[0]

        while slow != fast :
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
```