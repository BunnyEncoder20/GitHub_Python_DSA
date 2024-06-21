# Minimum Number of Coins

- Given a value `V`, if we want to make a change for ₹V, and we have an infinite supply of each of the denominations in Indian currency, i.e., we have an infinite supply of 
  - { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, 
- what is the minimum number of coins and/or notes needed to make the change.

<br>

## Brute Force Approach 

- We use a greedy approach 
- This Greedy approach will fail if the previous lesser denominations add up to be greates than the next denomination
- Eg:
```python
denominations = [1,5,6,7]
V = 11
Greedy_answer = [9,1,1] = 3 notes
Actual_answer = [5,6] = 2 notes
```
- The above scenario can only be solved using Dynamic Programming Approach.

### Algorithm
- [Watch it here](https://youtu.be/mVg9CfJvayM?si=kkhzOYbkXddJgBl_&t=148)
- If we need to make V amount, we must only use the denominations which are less than V
- Among the remaining, we need to make as many of the largest denomination we have for minimum number of coins 


### Code 

```python 
from typing import List

# Approach 1
def minimum_coins(change:int,coins:List[int])->int:
    n = len(coins)
    coins_used = []
    pointer = n-1
    while pointer>0 and change>0:
        if coins[pointer]<=change:
            change-=coins[pointer]
            coins_used.append(coins[pointer])
            continue
        pointer-=1
    return coins_used

# Approach 2
def minimum_coins2(change:int,coins:List[int])->List[int]:
    n = len(coins)
    coins_used = []
    for i in range(n-1,-1,-1):
        while coins[i]<=change:
            change-=coins[i]
            coins_used.append(coins[i])
    return coins_used

if __name__ == '__main__':
    V = 49
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    coins_used = minimum_coins(V,coins)
    print(f"The minimum number of notes requiried for {V} change is : {len(coins_used)}\nUsing the coins : ",coins_used)
```
- **Time complexity : O(v)**    (but it will generally take way lesser than that)
- **Space complexity : O(1)**

<br>

---
---