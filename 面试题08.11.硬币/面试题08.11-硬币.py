class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        coin = [1, 5, 10, 25]
        dp = [1] + [0] * n
        for c in coin:
            for i in range(c, n + 1):
                dp[i] += dp[i - c]
        return dp[-1] % (10**9 + 7)