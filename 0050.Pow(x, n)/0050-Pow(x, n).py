class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        i = abs(n)
        res = 1.0
        while(i != 0):
            if i % 2:
                res *= x
            x *= x
            # print i, res
            i /= 2
        return res if n > 0 else 1/res
        