class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # C(m + n - 2) (m - 1)
        k = m + n - 2
        t = m - 1
        
        up = 1
        for i in range(0, t):
            up *= k - i
        
        down = 1
        for i in range(1, m):
            down *= i
        
        # print up, down
        return up // down