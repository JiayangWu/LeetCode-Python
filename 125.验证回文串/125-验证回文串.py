class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                res += ch.lower()
        # print res
        return res == res[::-1]