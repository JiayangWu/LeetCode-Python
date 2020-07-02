class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(c ** 0.5) + 1):
            t = c - i ** 2
            s = int (t ** 0.5)
            if t == s ** 2:
                return True
        return False if c else True