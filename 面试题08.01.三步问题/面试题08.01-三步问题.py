class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 3)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        MOD = 10 ** 9 + 7
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD
        return dp[n]