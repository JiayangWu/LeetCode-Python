class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = matrix[i][0]
            res += dp[i][0]
            
        for j in range(1, n):
            dp[0][j] = matrix[0][j]
            res += dp[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    res += dp[i][j]
        print dp
        return res
            