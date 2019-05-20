class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        res = []
        # n = N
        while N:
            # b = N % -2
            # N = N //-2
            N, b = divmod(N, 2)
            N = -N
            res.append(str(b))
        return "".join(res[::-1]) or "0"
        # return "0" if not n else "".join(res[::-1])
