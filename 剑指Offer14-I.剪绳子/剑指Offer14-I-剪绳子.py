class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i][j] ba changdu wei i de shengzi qiecheng j duan de daan 
        if n == 2:
            return 1 
        if n == 3:
            return 2
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i 
        
        for i in range(n + 1):
            for j in range(i):
                for k in range(i + 1, n + 1):
                    dp[k][j + 1] = max((k - i) * dp[i][j], dp[k][j + 1])

        return max(dp[-1]) 


