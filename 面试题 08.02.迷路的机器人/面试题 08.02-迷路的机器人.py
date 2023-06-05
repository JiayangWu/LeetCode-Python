from collections import deque
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return []
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m -1][n - 1] == 1:
            return []

        self.res = []
        # dfs
        visited = set([(0, 0)])
        def dfs(i, j, path):
            if not 0 <= i < m or not 0 <= j < n:
                return
            path.append([i, j])
            if i == m - 1 and j == n - 1:
                self.res = path[:]
                return
            if not self.res:
                if i + 1 < m and obstacleGrid[i + 1][j] != 1 and (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    dfs(i + 1, j, path[:])
                if j + 1 < n and obstacleGrid[i][j + 1] != 1 and (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    dfs(i, j + 1, path[:])
        dfs(0, 0, [])             
        return self.res

        