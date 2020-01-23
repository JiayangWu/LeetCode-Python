class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0
        while a or b or c:
            if (a & 1 | b & 1) != (c & 1):
                res += 1 + (a & 1) * (b & 1)
            a, b, c = a >> 1, b >> 1, c >> 1
        return res