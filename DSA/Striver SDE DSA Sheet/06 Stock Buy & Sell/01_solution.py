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
        