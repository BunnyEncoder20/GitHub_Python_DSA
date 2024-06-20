# Fractional Knapsack Problem : Greedy Approach

- The weight of `N` items and their corresponding values are given. 
- We have to put these items in a knapsack of weight `W` such that the total value obtained is maximized.

**Note:** We can either take the item as a whole or break it into smaller units (Hence Fractional).

<br>

## Brute Force Approach

- We pick up those which give us the maximum value per unit weight

### Algorithm 

- Sort the array according to the per unit weight value in decreasing order
- Pick up the units and keep in knapsack if we have that much weight left 
- Keep updating the value
- When we cannot pick up the entire value, we put it's fractional value

### Code 

```python
from typing import List

class Item:
    def __init__(self,value,weight) -> None:
        self.value = value
        self.weight = weight

def fractionalKnapsack(W,arr:List[int],n)->int:
    arr.sort(key=lambda x:x.value/x.weight,reverse=True)
    sack_value = 0
    current_weight = 0
    for i in range(n):
        if arr[i].weight+current_weight<=W:
            sack_value += arr[i].value
            current_weight+=arr[i].weight
        else:
            remaining_weight = W-current_weight
            sack_value += (arr[i].value/arr[i].weight)*remaining_weight
            break
    return sack_value 


if __name__ == '__main__':
    n = 3
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    ans = fractionalKnapsack(W, arr, n)
    print("The maximum value is", ans)
```
- **Time complexity : O(nlogn) + O(n)**
- **Space complexity : O(1)**