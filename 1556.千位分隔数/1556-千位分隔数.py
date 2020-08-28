class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)[::-1]
        res = ""
        for i in range(len(s)):
            res += s[i]
            if i % 3 == 2 and i != len(s) - 1:
                res += "."
        return res[::-1] 