class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        self.res = 0
        self.tmp = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        def dfs(x0, y0):
            self.tmp += 1
            self.res = max(self.res, self.tmp)
            
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x< m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 0
                    dfs(x, y)
                    
                
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    self.tmp = 0
                    dfs(i, j)
        return self.res