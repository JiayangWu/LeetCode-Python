class Solution(object):
    def myPow(self, x0, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        def helper(x, n, tmp):
            print n, x
            if n <= 1:
                return x * tmp
            if n % 2:
                tmp *= x
                n -= 1
            return helper(x * x, n // 2, tmp)
        op = 1
        if n < 0:
            op = -1 
        res = helper(x0, abs(n), 1)
        return res if op > 0 else 1.0/res