class Solution(object):
    def numIslands(self, M):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        m, n = len(M), len(M[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        # print visited
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        res = 0
        
        def dfs(x0, y0):
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                # print x, y
                if 0<= x < m and 0 <= y < n and M[x][y] == '1' and visited[x][y] ==0:
                    visited[x][y] = 1
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if M[i][j] == '1' and visited[i][j] == 0:
                    res += 1
                    visited[i][j] = 1
                    dfs(i, j)
                    # print visited
                    
        return res