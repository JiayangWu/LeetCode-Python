class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            tmp = self.centralSpread(i, i, s)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.centralSpread(i, i + 1, s)
            if len(tmp) > len(res):
                res = tmp
        return res

    def centralSpread(self, left, right, s):
        res = ""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res = s[left: right + 1]
            left -= 1
            right += 1
        # print res, left, right
        return res