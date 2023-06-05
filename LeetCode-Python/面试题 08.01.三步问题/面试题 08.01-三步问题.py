class Solution:
    def waysToStep(self, n: int) -> int:
        dp = [0] * (max(10, n + 1))
        MOD = 10 ** 9 + 7
        dp[1], dp[2], dp[3] = 1, 2, 4
        for i in range(4, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD
        return dp[n]