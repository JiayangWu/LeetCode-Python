class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0, len(s) - 1):
            if s[:i + 1] * (len(s) //(i + 1)) == s:
                return True
        return False