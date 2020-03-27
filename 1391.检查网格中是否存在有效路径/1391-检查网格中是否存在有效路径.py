class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        dir = {}
        dir[1] = [0, 1, 0, 1]
        dir[2] = [1, 0, 1, 0]
        dir[3] = [0, 0, 1, 1]
        dir[4] = [0, 1, 1, 0]
        dir[5] = [1, 0, 0, 1]
        dir[6] = [1, 1, 0, 0]

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        queue = [(0, 0)]
        visited = set(queue)
        
        cor = {0:2, 1:3, 3:1, 2:0}
        while queue:
            x0, y0 = queue.pop()
            if [x0, y0] == [m - 1, n - 1]:
                return True
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and dir[grid[x0][y0]][k] & dir[grid[x][y]][cor[k]]:
                    visited.add((x, y))
                    queue.append((x, y))
        return False

