class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = min(A)
        s = 0
        while n > 0:
            n, tmp = divmod(n, 10)
            s += tmp
        # print s
        return 1 - s % 2