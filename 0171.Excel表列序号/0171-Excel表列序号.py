class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i, char in enumerate(s):
            res *= 26
            res += 1 + ord(char) - ord("A")           
        return res