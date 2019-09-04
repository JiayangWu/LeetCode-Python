class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [0] * (n + 3)
        dp[0], dp[1], dp[2] = 0, k, k * k
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)
        return dp[n]