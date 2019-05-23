class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        record = [0]#一开始从开头开始找
        
        for j in range(len(s) + 1):
            for i in record:#在之前每一种找法的基础上找
                if s[i : j] in wordDict: #找到一种可行的分法，说明最远可以拆分到j
                    record.append(j)
                    break
        # print record
        return record[-1] == len(s)
                