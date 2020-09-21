class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import deque
        if not matrix or not matrix[0]:
            return matrix 
        m, n = len(matrix), len(matrix[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        res = [[0 for _ in range(n)] for _ in range (m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    queue = deque([(i, j, 0)])
                    visited = set((i, j))
                    while queue:
                        x, y, dist = queue.popleft()

                        if matrix[x][y] == 0:
                            res[i][j] = dist 
                            break
                        else:
                            for k in range(4):
                                xx = x + dx[k]
                                yy = y + dy[k]

                                if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in visited:
                                    visited.add((xx, yy))
                                    queue.append((xx, yy, dist + 1))
        
        return res