class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2:
            return "a" * n
        return "a" * (n - 1) + "b"