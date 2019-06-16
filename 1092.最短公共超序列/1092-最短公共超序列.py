class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        #先找到最长公共子序列
        l1, l2 = len(str1), len(str2)
        if l1 < l2:
            l1, l2 = l2, l1
            str1, str2 = str2, str1
        common = self.findLCS(str1, str2)  
        # print common
        res = ""
        str1_idx = 0
        str2_idx = 0
        for char in common:
            while str1_idx < l1 and str1[str1_idx] != char:
                res += str1[str1_idx]
                str1_idx += 1
            while str2_idx < l2 and str2[str2_idx] != char:
                res += str2[str2_idx]
                str2_idx += 1
            res += char
            str1_idx += 1
            str2_idx += 1
            
        if str1_idx != l1:
            res += str1[str1_idx:]
        if str2_idx != l2:
            res += str2[str2_idx:]
        return res

    def findLCS(self, str1, str2):
        m, n = len(str1), len(str2)
        dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]: #匹配上了
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                elif len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                elif len(dp[i - 1][j]) <= len(dp[i][j - 1]):
                    dp[i][j] = dp[i][j - 1]

        return dp[m][n]
