class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [0]
        
        for j in range(len(s) + 1):
            for i in dp:
                if s[i:j] in wordDict:
                    dp.append(j)
                    break
        # print dp
        return dp[-1] == len(s)
                    