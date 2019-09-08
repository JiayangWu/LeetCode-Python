class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #dp[i][j]表示word1[:i + 1]和word2[:j + 1]的解
        l1, l2 = len(word1), len(word2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        
        for i in range(l1 + 1):
            dp[i][0] = i
        for j in range(l2 + 1):
            dp[0][j] = j
            
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
        return dp[l1][l2]
        
    