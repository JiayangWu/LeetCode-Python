class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -2 **31
        INT_MAX = 2 ** 31 - 1
        op = 1
        if x < 0:
            op = -1
            s = str(x)[1:]
        else:
            s = str(x)
            
        res = op * int(s[::-1])
        return res if INT_MIN <= res <= INT_MAX else 0
            
        