class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s0, s1, s2 = 0, 0, 0
        n = len(grid)
        
        for i in grid:
            s0 += n - i.count(0)
            s1 += max(i)
        
        for i in zip(*grid):
            s2 += max(i)
        
        return s0 + s1 + s2