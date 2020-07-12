class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, int(i ** 0.5 + 1)):
                if not dp[i - j * j]:
                    dp[i] = 1
                    break
        return dp[n] == 1
                    