class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # print i, j
                dp[i][j] = grid[i][j]
        
        
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
                elif i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                elif j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]