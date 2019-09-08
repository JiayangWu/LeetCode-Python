class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for _ in range(m)]for _ in range(n)]
        
        for i in range(m):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[j][0] != 1:
                
                dp[j][0] = 1
            else:
                break
            
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]