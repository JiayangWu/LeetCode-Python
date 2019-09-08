class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        for i, price in enumerate(prices):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -price
            else:
                # tmp = dp[i][0]
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            # print dp        
        return dp[i][0] if prices else 0