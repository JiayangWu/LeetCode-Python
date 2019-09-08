class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_k = 2
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(max_k + 1)] for _ in range(n)]
        
        for i, price in enumerate(prices):
            for k in range(max_k, 0, -1):
                if i == 0:
                    dp[0][k][0] = 0
                    dp[0][k][1] = -price
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
                
        return dp[n - 1][max_k][0] if prices else 0