class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #用dp[i][j]表示word1[:i + 1], word2[:j + 1]这个问题的解
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m + 1): 
            dp[i][0] = i
            
        for i in range(n + 1):
            dp[0][i] = i
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) #分别对应插入，替换，删除
                    
        return dp[m][n]