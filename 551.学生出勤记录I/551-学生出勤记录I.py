class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count("A") <= 1 and "LLL" not in s