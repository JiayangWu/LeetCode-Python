class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #dp[i][k][1/0]表示第i天还可以交易k次手上持有或没持有股票的状态
        #对于第二题，k = 2
        #dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + price[i])
        #dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - price[i])
        #当k = 0时， dp[i][0][1/0] = 0
        dp = [[0 for _  in range(2)] for _ in range(len(prices))]
        
        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        
        # print dp
        return dp[len(prices) - 1][0] if prices else 0