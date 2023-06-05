class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col_grid = [list(col) for col in zip(*grid)]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                res += min(max(grid[i]), max(col_grid[j])) - grid[i][j]
        return res