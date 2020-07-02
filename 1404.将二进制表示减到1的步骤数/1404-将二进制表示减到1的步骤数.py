class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        s = int(s, 2)
        while s != 1:
            cnt += 1
            if s % 2:
                s += 1
            else:
                s //= 2
        return cnt