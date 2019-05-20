class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #dp[m][n] = min(dp[m - 1][n], dp[m][n - 1]) + grid[m][n]
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * (n)] * (m) 
        for i in range(m):
            for j in range(n):
                # print dp, i, j
                if not i and not j:
                    dp[i][j] = grid[i][j]
                elif i and not j:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif not i and j:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]