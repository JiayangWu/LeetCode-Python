class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        if not grid or not grid[0]:
            return False
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True