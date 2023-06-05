class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        if not grid or not grid[0]:
            return -1
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        
        # BFS
        dx = [0, 0, 1, 1, 1, -1, -1, -1]
        dy = [1, -1, 1, 0, -1, 1, 0, -1]

        visited = set([(0, 0)])
        queue = deque([((0, 0), 1)]) # (x, y), step

        while queue:
            cur = queue.popleft()
            x, y, step = cur[0][0], cur[0][1], cur[1]

            if [x, y] == [n - 1, n - 1]:
                return step

            for i in range(8):
                xx, yy = x + dx[i], y + dy[i]
                if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] == 0 and (xx, yy) not in visited:
                    visited.add((xx, yy))
                    queue.append(((xx, yy), step + 1))
        
        return -1

