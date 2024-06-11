# Largest Sub Array with K Sum 

- Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.
- Example :
> Input:
> N = 8
> A[] = {15,-2,2,-8,1,7,10,23}
> Output: 5
> Explanation: The largest subarray with sum 0 will be -2 2 -8 1 7.
- Remember that **subArray = contigous part of the array.**

<br>

## Brute Force Approach 

### Algorithm 
- [Watch it here](https://youtu.be/frf7qxiN2qU?si=9o4CR7AICMFFhjzd&t=221)
- Generate all the subarrays.
- Check sum of the subarrays.
- Check if it longest subarray.

### Code 

```python
class Solution:
    def maxLen(self, n, arr):
        target = n 
        n = len(arr)
        longest = 0

        # Generating all the sub array
        for i in range(n):
            for j in range(i+1,n):
                subarray = arr[i:j+1]
                total = sum(subarray)

                if total==target :
                    longest = max(longest,(j-i+1)) 
        
        return longest


if __name__ == "__main__":
    i = Solution()
    n,arr=8,[15,-2,2,-8,1,7,10,23]
    print(i.maxLen(n,arr))
```
- Time complexity : O(n<sup>3</sup>)
- Space complexity : O(1)
- But we can optimize our brute using the observation : 
    - we don't need to sum the entire subarray always
    - Just add the new element, to the previous calculated sum.

```python 
class Solution:
    def maxLen(self, n, arr):
        target = n 
        n = len(arr)
        longest = 0

        # Generating all the sub array
        for i in range(n):
            total = 0
            for j in range(i+1,n):
                total += arr[i]
                if total==target :
                    longest = max(longest,(j-i+1)) 
        return longest


if __name__ == "__main__":
    i = Solution()
    n,arr=8,[15,-2,2,-8,1,7,10,23]
    print(i.maxLen(n,arr))
```
- **Time complexity : O(n<sup>2</sup>)**
- **Space complexity : O(1)**

<br>

## Better Approach 

### Algorithm

- [Watch it here](https://youtu.be/frf7qxiN2qU?si=O94vP8pESnJwjouM&t=652)
-  Store the the sum till that element in a hashmap.
- For a Sum , check if Sum-K is present in the hashmap. If yes, then current_index-store_index will be the length of the subarray which has the sum = k
- Remember not to update the sum into the hashmap if a previous index already exists 
- Update the longest length 
- **If the array contains negative,0 and postives, then this is the optimal solution.**

### Code 

```python
class Solution:
    def maxLen(self, target, arr):
        n = len(arr)
        hashmap = {}
        summation = 0
        longest = 0

        for i in range(n) : 
            summation+=arr[i]
            if summation == target : 
                length = i+1
                longest = max(longest,length)
            
            required = summation - target
            if required in hashmap : 
                length = i - hashmap[required]
                longest = max(longest,length)
            
            if summation not in hashmap : 
                hashmap[summation] = i    # import, do not update the sum for a newer index, as we need the longest, Hence the left most index 

        return longest

if __name__ == "__main__":
    i = Solution()
    n,arr=8,[15,-2,2,-8,1,7,10,23]
    print(i.maxLen(n,arr))
```
- **Time complexity : O(n * log(n)) or O(n * 1)** 
- Order map = O(log(n))
- Unorderd map = O(1) 
- Unordered map worst case will result in O(n), resulting in a overall complexity of **O(n<sup>2</sup>)**
- **Space complexity : O(n)**   (for the hashmap)
- **NOTE :** This is the **optimal solution** if the array includes **0 and negative integers.**

<br>

## Optimal Approach 

- If the array only contains positive integers.

### Algorithm
- [Watch it here](https://youtu.be/frf7qxiN2qU?si=qVMitmjMjAzGrSei&t=1731)
- 2 pointer greedy approach
- keep incrase the pointer in front till the sum is greater than target
- if the sum becomes greater than target, start moving the pointer at the back till sum<=target
- If the sum becomes < target, start increasing the pointer in front again.

### Code 

```python 
class Solution:
    def maxLen(self, target, arr):
        n = len(arr)
        front,back = 0,0
        current_sum = 0
        longest = 0

        while front<n : 
            # add the current element to sum
            current_sum += arr[front]

            # if the sum > target, move the back pointer
            while current_sum > target : 
                current_sum -= arr[back]
                back+=1
            
            # if the sum = target
            if current_sum == target:
                longest = max(longest,front-back+1)
            
            # if the sum < target, move the front pointer
            front += 1

        return longest 
    
if __name__ == "__main__":
    i = Solution()
    n,arr=3,[1,2,3,1,1,1,1]
    print(i.maxLen(n,arr))
```
- **Time complexity : O(2n)** (the second loop runs for n times overall)
- **Space complexity : O(1)**