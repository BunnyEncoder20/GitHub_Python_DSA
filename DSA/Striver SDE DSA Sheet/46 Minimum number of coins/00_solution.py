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
    # coins_used = minimum_coins(V,coins)
    coins_used = minimum_coins2(V,coins)
    print(f"The minimum number of notes requiried for {V} change is : {len(coins_used)}\nUsing the coins : ",coins_used)