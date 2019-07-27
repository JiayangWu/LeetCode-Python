class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversedS = s[::-1]
        i = 0
        for i in range(len(s)):
            if reversedS[i:] == s[:len(s) - i]:
                return reversedS[:i] + s
        return ""