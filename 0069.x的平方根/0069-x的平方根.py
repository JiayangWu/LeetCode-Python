class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x :
            return 0
        if x < 4:
            return 1
        start, end = 2, x // 2
        while 1:
            i = (start + end) // 2
            if i ** 2 <= x and (i + 1) ** 2 >x:
                return i
            elif i ** 2 < x:
                start = i + 1
            elif i ** 2 > x:
                end = i - 1
                
                