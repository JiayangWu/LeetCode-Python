class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         dp[i][k][0] = max(dp[i – 1][k][0], dp[I – 1][k][1] + prices[i])
#         dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k][0] - prices[i])
#         第一题 k = 1

#         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
#         dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

#         当i = 0时，
#         dp[0][0] = 0
#         dp[0][1] = -prices[0]
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        for i, price in enumerate(prices):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -price
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1],  - prices[i])
                
        return dp[len(prices) - 1][0] if prices else 0
            