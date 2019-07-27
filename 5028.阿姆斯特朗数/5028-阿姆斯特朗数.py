class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        k = len(str(N))
        n = N
        s = 0
        while N:
            N, tmp = divmod(N, 10)
            s += tmp ** k
        return s == n