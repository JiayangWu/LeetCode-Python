class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = n // 2
        if n % 2:
            return 2 * k + k * (k - 1) // 2 * 2
        else:
            return 1 * k + k * (k - 1) // 2 * 2
        