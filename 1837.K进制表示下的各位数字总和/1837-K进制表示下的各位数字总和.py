class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 0
        while n:
            res += n % k
            n //= k
        return res