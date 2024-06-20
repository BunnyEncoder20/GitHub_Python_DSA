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