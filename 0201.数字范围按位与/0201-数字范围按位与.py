class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or m == n:
            return m
        else: #当n > m的时候，因为相邻两个数 &的结果的最后一位必定为1，因此可以递归处理
            return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1
        
            