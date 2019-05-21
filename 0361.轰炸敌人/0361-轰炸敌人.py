class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        def count(x0, y0):
            cnt = 0
            for x in range(x0, -1, -1): #向上
                if grid[x][y0] == "E":
                    cnt += 1
                elif grid[x][y0] == "W":
                    break
                    
            for x in range(x0, m):  #向下
                if grid[x][y0] == "E":
                    cnt += 1
                elif grid[x][y0] == "W":
                    break
                    
            for y in range(y0, -1, -1): #向左
                if grid[x0][y] == "E":
                    cnt += 1
                elif grid[x0][y] == "W":
                    break      
                     
            for y in range(y0, n): #向右
                if grid[x0][y] == "E":
                    cnt += 1
                elif grid[x0][y] == "W":
                    break   
                    
            return cnt
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    res = max(res, count(i, j))
        return res