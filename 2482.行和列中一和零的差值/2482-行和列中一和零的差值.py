class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row2one = {}
        col2one = {}
        for i, row in enumerate(grid):
            row2one[i] = sum(row)
        for j, col in enumerate(zip(*grid)):
            col2one[j] = sum(col)

        diff = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = row2one[i] + col2one[j] - (n - row2one[i]) - (m - col2one[j])
        return diff