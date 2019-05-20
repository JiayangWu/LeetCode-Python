class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        r = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r += 4
                    if i < m-1 and grid[i+1][j] == 1:
                        r -= 2
                    if j < n-1 and grid[i][j+1] == 1:
                        r -= 2
        return r