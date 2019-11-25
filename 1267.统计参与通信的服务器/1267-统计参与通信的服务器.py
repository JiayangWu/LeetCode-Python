class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # horizontal
                    for col in range(n):
                        if col != j:
                            if grid[i][col] in [1, 2]:
                                grid[i][j] = 2
                                grid[i][col] = 2
                    
                    # vertical
                    for row in range(m):
                        if row != i:
                            if grid[row][j] in [1, 2]:
                                grid[i][j] = 2
                                grid[row][j] = 2
                if grid[i][j] == 2:
                    res += 1
        # print grid
        return res