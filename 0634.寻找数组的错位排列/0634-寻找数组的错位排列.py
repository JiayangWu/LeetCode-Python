class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(n + 1):
            res = (i * res + (-1) ** i) % (10 ** 9 + 7)
        return res