class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        def dfs(x, y):
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == "1":
                    grid[xx][yy] = "0"
                    dfs(xx, yy)
        
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    dfs(i, j)
                    res += 1
        return res