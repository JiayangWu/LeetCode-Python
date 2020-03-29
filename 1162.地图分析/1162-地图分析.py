class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        m, n = len(grid), len(grid[0])
        land = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land.append((i, j))

        if not land or len(land) == m * n:
            return -1 
        
        res = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        queue = deque(land)
        visited = set(land)
        while queue:
            for _ in range(len(queue)):
                x0, y0 = queue.popleft()

                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]

                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                        queue.append((x, y))
                        visited.add((x, y))
            res += 1
        return res - 1

        