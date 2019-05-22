class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while(i<num):
            i*= 4
        return i == num
        