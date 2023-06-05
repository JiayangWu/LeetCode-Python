from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # print n

        if grid[0][0] or grid[-1][-1] == 1:
            return -1
        queue = deque([[[0, 0], 1]])
        # queue2 = deque([[[n -1 , n - 1], 1]])
        visited = set((0,0))
        dx = [1, -1, 0, 0, 1, -1, -1, 1]
        dy = [0, 0, 1, -1, -1, 1, -1, 1]
        cnt = 1
        record = dict()
        while queue:
            cur, cnt = queue.popleft()
            # print cur, cnt
            x0, y0 = cur[0], cur[1]
            
            if x0 == n - 1 and y0 == n - 1:
                return cnt
            for k in range(8):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x <n and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                    visited.add((x, y))
                    queue.append([[x, y], cnt + 1])
        return -1
        