class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        from collections import deque

        if not rooms or not rooms[0]:
            return rooms
        INF = 2147483647

        m, n = len(rooms), len(rooms[0])
        queue = deque() # (x_pos, y_pos, step from a gate)
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while queue:
            x_pos, y_pos, step = queue.popleft()
            for k in range(4):
                x = x_pos + dx[k]
                y = y_pos + dy[k]

                if 0 <= x < m and 0 <= y < n and rooms[x][y] == INF:
                    rooms[x][y] = step + 1
                    queue.append((x, y, step + 1))