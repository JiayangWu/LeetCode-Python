class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    res += 1
                    
                    queue = deque([(i, j)])

                    while queue:
                        x0, y0 = queue.popleft()
                        for k in range(4):
                            x = x0 + dx[k]
                            y = y0 + dy[k]

                            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                                grid[x][y] = "0"
                                queue.append((x, y))

        return res