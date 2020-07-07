class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 3)]
        dp[0] = n
        dp[1] = k
        dp[2] = k * k
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)
        return dp[n]