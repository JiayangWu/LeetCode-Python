class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 1
        while(i<n):
            i*=2
        return i == n
        