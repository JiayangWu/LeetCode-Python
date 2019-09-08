class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        
        dp = [len(s) for i in range(len(s))]
        for i in range(0, len(s)):
            self.centeralExtend(s, i, i, dp)
            self.centeralExtend(s, i, i+1, dp)
        print dp
        return dp[-1]
    
    def centeralExtend(self, string, left, right, dp):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            if left > 0:
                dp[right] = min(dp[right], dp[left - 1] + 1)
            else:
                dp[right] = 0
            left -= 1
            right += 1
                