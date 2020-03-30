class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n == 1:
            return 0
        return (self.lastRemaining(n - 1, m) + m) % n