class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [-1] # dp[i] 表示从0~下标为i的单词可以被拆分
        
        for i, ch in enumerate(s):
            for start in dp:
                if s[start + 1:i + 1] in wordDict:
                    dp.append(i)
                    break

        return dp[-1] == len(s) - 1