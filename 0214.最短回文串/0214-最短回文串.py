class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversedS = s[::-1]
        # print reversedS
        i = 0
        for i in range(len(s)):
            # print reversedS[i:], s[:len(s) - i]
            if reversedS[i:] == s[:len(s) - i]:
                return reversedS[:i] + s
        return ""