class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp[i] represents res for s[:i]
        dp = [i for i in range(len(s) + 1)]

        for i in range(len(s) + 1):
            dp[i] = min(dp[i], dp[i - 1] + 1)
            for d in dictionary:
                if i >= len(d) and s[i - len(d):i] == d:
                    dp[i] = min(dp[i], dp[i - len(d)])

        return dp[-1]
                    

        