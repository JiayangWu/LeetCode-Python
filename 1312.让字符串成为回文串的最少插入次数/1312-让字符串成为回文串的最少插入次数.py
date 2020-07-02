class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s) - self.longestPalindromeSubseq(s)
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j + 1] + 2
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i - 1][j])
        return dp[n - 1][0]