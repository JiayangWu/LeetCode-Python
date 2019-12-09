class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        res = 0
        for j in range(n):
            if matrix[0][j]:
                res += 1
                dp[0][j] = 1
        
        for i in range(1, m):
            if matrix[i][0]:
                res += 1
                dp[i][0] = 1
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res += dp[i][j]
        return res