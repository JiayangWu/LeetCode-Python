class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)[2:]
        last_one, res = 0, 0
        for i, char in enumerate(b):
            if char == "1":
                res = max(res, i - last_one)
                last_one = i
                
        return res
        