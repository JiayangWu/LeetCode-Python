class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = len(image), len(image[0])
        visited = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        self.min_x, self.min_y, self.max_x, self.max_y = 0, 0, 0, 0
        
        def dfs(x0, y0):
            # print (self.min_x, self.min_y, self.max_x, self.max_y, x0, y0)
            self.min_x = min(self.min_x, x0)  
            self.max_x = max(self.max_x, x0)
            self.min_y = min(self.min_y, y0)  
            self.max_y = max(self.max_y, y0)
            visited[x0][y0] = 1
            
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and visited[x][y] == 0 and image[x][y] == "1":
                    dfs(x, y)
            
        for i in range(m):
            for j in range(n):
                if image[i][j] == "1":
                    self.min_x, self.min_y, self.max_x, self.max_y = i, j, i, j
                    dfs(i, j) #因为全部相连，所以一次主体DFS之后就可以返回
                    # print (self.min_x, self.min_y, self.max_x, self.max_y)        
                    return (self.max_x - self.min_x + 1) * (self.max_y - self.min_y + 1)