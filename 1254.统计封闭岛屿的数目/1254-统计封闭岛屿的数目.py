class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        def dfs(x0, y0):
            if grid[x0][y0] == 0:
                grid[x0][y0] = -1
                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]
                    
                    if 0 < x < m and 0 < y < n and grid[x][y] == 0:
                        dfs(x, y)
                        
        for j in range(n):
            dfs(0, j)
        for j in range(n):
            dfs(m - 1, j)
        for i in range(m):
            dfs(i, 0)
        for i in range(m):
            dfs(i, n - 1)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res
            
        