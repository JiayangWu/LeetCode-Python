class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = 1
        while t < n:
            t *= 3
        return n == t