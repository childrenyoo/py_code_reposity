class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyin=10e9
        profit=0
        for i in range(1,len(prices)):
            buyin=min(buyin,prices[i-1])
            profit=max(profit,prices[i]-buyin)
        return profit
prices=[7,1,5,3,6,4]
s=Solution()
print(s.maxProfit(prices))