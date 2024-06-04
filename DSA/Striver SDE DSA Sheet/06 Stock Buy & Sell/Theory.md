# Best Time for buying and selling Stock

## Poblem 
- Problem basically states that if the indexes are treated as days and the values are treated as Price of the stocks on those days , then what is the correct time to buy and sell the stock. 
- Note that you cannot sell before you buy. 
- Eg: 
```python 
prices = [7,1,5,3,6,4]
buy = day 2 (i=1,price=1)
sell = day 5 (i=4,price=6)
profit = 6-1 = 5
Answer = 5
```
- The problem states that we have to maximize the profit

---

## Algorithm 

- **Note:** if you are selling on i<sup>th</sup> then you'll buy on the minimum price from (1)day to (i-1) day 
- Hence intuition of the algo is to keep track of the minimum number on the right side of the arr.
- Substract the current value with the minimum on the right to get the profit and check if it more then previous profit.
- Before going to the next iter, check to see if the current value is lesser than minimum. 

---

## Code

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        profit,cost = 0,0

        for i in range(0,len(prices)):
            cost = prices[i]-mini
            profit = max(profit,cost)
            mini = min(mini,prices[i])

        return profit 

if __name__ == "__main__":
    pricesList = [[7,1,5,3,6,4],[7,6,4,3,1]]
    ins = Solution()
    for prices in pricesList :
        print(ins.maxProfit(prices))
```