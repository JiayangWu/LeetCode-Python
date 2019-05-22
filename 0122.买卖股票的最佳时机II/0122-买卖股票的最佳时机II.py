class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit = prices[i] - prices[i-1]
                sum += profit
        return sum