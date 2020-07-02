class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))

        res = 0
        while queue:     
            for i in range(len(queue)):
                pair = queue.popleft()
                x0, y0 = pair[0], pair[1]
                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]

                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append((x, y))
            if not queue:
                break
            res += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return res
                    
        
        