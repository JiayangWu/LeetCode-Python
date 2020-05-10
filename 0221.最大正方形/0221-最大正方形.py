class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for j in range(n):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                res = 1
        
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                res = 1
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    res = max(res, dp[i][j] ** 2)
        # print dp
        return res