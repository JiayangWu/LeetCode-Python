import math
class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 6
        
        res = 0
        cnt = N
        op = 1
        while(N >= 4):
            res += int(math.floor(N * (N - 1) / (N -2)) * op)
            res += N - 3
            if op == 1:
                op = -1
            N -= 4
        
        
        if N == 0:
            return res
        elif N == 1:
            return res - 1
        elif N == 2:# 6 *5 /4 +3-2*1
            return res - 2
        else: #7*6/5+4-3*2/1
            return res - 6
            