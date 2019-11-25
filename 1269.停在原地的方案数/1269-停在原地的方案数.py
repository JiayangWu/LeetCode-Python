class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        # dp[i][j] 代表走 i 步，到位置 j 的解
        # dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
        n = min(steps, arrLen)
        dp = [[0 for _ in range(n)] for _ in range(steps + 1)]
        mod = 10 ** 9 + 7
        
        dp[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(n):
                if j == 0:
                    dp[i][j] += (dp[i - 1][0] + dp[i - 1][1]) % mod
                elif j == n - 1:
                    dp[i][j] += (dp[i - 1][j] + dp[i - 1][j - 1]) % mod
                else:
                    dp[i][j] += (dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1])  % mod                         
        return dp[steps][0]