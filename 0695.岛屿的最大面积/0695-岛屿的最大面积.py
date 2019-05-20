class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        
        def dfs(x, y):
            
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                                
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1:
                    grid[xx][yy] = 2 #来过了就染色为2
                    self.temp += 1
                    dfs(xx,yy)
                       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 2 #来过了就染色为2
                    self.temp = 1
                    dfs(i, j)
                    res = max(res, self.temp)
                    
        return res