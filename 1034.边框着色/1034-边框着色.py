class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """

        m= len(grid)
        if not m:
            return grid
        n = len(grid[0])
        if not n:
            return grid
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        originalcolor = grid[r0][c0]
        record = list()
        visited = list()
        for row in grid:
            record.append(row[:])
            visited.append(row[:])
            
        def checkNeibor(x, y):     
            #返回4说明不染色，返回其他说明满足染色条件
            if x in [0, m - 1] or y in [0, n - 1]:#在边界上
                return -1
            cnt = 0
            for j in range(4):
                xx = x + dx[j]
                yy = y + dy[j]
                if 0 <= xx < m and 0<= yy < n and originalcolor == record[xx][yy]:
                    cnt += 1
            return cnt 
  
        if checkNeibor(r0, c0) != 4:
            grid[r0][c0] = color
        
        queue = [[r0,c0]]
        while(queue):
            newqueue = list()
            for node in queue:
                x0 = node[0]
                y0 = node[1]
                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]

                    if 0 <= x < m and 0<= y < n and originalcolor == record[x][y] and visited[x][y] != -1:
                        newqueue.append([x, y])
                        visited[x][y] = -1
                        # print [x, y], queue
                        if checkNeibor(x, y) != 4:
                            grid[x][y] = color           
                        
            queue = newqueue[:]
        
        return grid