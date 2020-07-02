class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        
        size = m * n
        k = k % size  
        l = [grid[i][j] for i in range(m) for j in range(n)]
           
        l = l[-k:] + l[:-k]
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = l[i * n + j]
        return grid