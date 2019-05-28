from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m, n = len(image), len(image[0])
        color = image[sr][sc]
        image[sr][sc] = newColor
        
        visited = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        q = deque()
        q.append([sr,sc])
        while q:
            x0, y0 = q.popleft()
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]

                if 0 <= x < m and 0 <= y < n and image[x][y] == color and visited[x][y] == 0:
                    image[x][y] = newColor
                    visited[x][y] = 1
                    q.append([x, y])
                    
        return image