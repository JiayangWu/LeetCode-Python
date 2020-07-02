class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m, n = len(grid), len(grid[0])
        visited = set()
        self.res = 0
        
        def dfs(x0, y0, tmp):
            self.res = max(self.res, tmp)
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    value = grid[x][y]
                    grid[x][y] = -1
                    dfs(x, y, tmp + value)
                    grid[x][y] = value
                    
        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                grid[i][j] = -1
                dfs(i, j, value)
                grid[i][j] = value
        return self.res