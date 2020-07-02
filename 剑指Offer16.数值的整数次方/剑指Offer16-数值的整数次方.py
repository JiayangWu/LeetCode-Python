class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x 
        if n == 2:
            return x * x

        flag = 0
        if n < 0:
            flag = 1
            n = -n

        if n % 2 == 0:
            res = self.myPow(self.myPow(x, n // 2), 2)
        else:
            res = self.myPow(self.myPow(x, n // 2), 2) * x

        return res if not flag else 1.0 / res