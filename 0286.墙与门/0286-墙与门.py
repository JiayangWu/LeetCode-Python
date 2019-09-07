class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        from collections import deque
        if not rooms or not rooms[0]:
            return rooms
        m, n = len(rooms), len(rooms[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        INF = 2147483647
        queue = deque()
        def bfs(queue):
            while queue:
                pos = queue.popleft()
                x0, y0 = pos
                    
                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == INF:
                        rooms[x][y] = rooms[x0][y0] + 1
                        queue.append((x, y))
                
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0: #现在从每扇门出发
                    queue.append((i, j))
        bfs(queue)
        return rooms