class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j] 
        dp = [len(s) for _ in range(len(s) + 1)]
        dp[0] = -1
        for i in range(len(s)):
            for j in range(i + 1):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    dp[i + 1] = min(dp[j] + 1, dp[i + 1])
        # print dp
        return dp[-1]