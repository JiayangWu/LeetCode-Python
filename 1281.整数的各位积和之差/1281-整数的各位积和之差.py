class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product, s = 1, 0

        while n:
            n, digit = divmod(n, 10)
            product *= digit 
            s += digit
        return product - s