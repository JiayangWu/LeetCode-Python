class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        # 1 +2 + 3 + ... + k = (k + 1) * k / 2 < n
        return (-1 + int(math.sqrt(1 + 8 * n))) // 2