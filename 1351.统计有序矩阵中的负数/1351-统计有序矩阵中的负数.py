class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    res += 1
        return res