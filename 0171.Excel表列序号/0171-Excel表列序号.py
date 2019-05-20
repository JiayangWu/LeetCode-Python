class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s) - 1
        res = 0
        for index, item in enumerate(s):
            res += (ord(item) - ord("A") + 1) * (26 ** (l - index))
        return res
            