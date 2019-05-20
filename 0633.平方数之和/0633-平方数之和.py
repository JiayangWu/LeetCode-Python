class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        if c == (int(c ** 0.5) ** 2):
            return True
        
        lo, hi = 0, int(c ** 0.5)
        while(lo <= hi):
            s = lo ** 2 + hi ** 2
            if s == c:
                return True
            elif s > c:
                hi -= 1
            else:
                lo += 1
        return False
        