class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        if length == 0:
            return 0
        res = 0

        for i in range(0, length):
            for j in range(0, length):
                rowMax = 0
                colomnMax = 0
                for t in range(0,length):
                    rowMax = max(grid[i][t],rowMax)
                    colomnMax = max(grid[t][j],colomnMax)
                print rowMax, colomnMax
                res += min(colomnMax,rowMax ) - grid[i][j]
        return res
                