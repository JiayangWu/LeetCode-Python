class Solution(object):
    def isFlipedString(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return s1 in s2 + s2 and len(s1) == len(s2)