class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        rotlist = list()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotlist.append([i, j])
        minute = 0
        while(rotlist):
            newrotlist = list()
            for rotnode in rotlist:
                x0 = rotnode[0]
                y0 = rotnode[1]
                
                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]
                    
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        newrotlist.append([x,y])
            if not newrotlist:
                break
                
            rotlist = newrotlist[:]
            minute += 1
            
        for row in grid:
            for i in row:
                if i == 1:#还有新鲜的
                    return -1
        return minute
            