class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0: res += 2 # 上和下
                for r in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= r[0] < len(grid) and 0 <= r[1] < len(grid[0]): res += max(0, grid[i][j] - grid[r[0]][r[1]]) # 中间高出相邻方块的部分
                    else: res += grid[i][j] # 前后左右最外侧

        return res