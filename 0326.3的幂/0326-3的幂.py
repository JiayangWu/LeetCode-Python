class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 1
        while(i<n):
            i *= 3
        return i == n
            
        