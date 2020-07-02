class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1 

        res, MOD = 1, 10 ** 9 + 7
        while n > 4:
            res = (res * 3) % MOD
            n -= 3

        return res * n % MOD