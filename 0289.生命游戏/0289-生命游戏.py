class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return board
        n = len(board[0])
        if n == 0:
            return board
        
        alivex = list()
        alivey = list()
        
        def neibor(x, y): #统计八个邻居里有几个是活细胞（1）
            dx = [1, -1, 0, 0, 1, -1, -1, 1]
            dy = [0, 0, 1, -1, 1, -1, 1, -1]
            
            cnt = 0
            for k in range(8):
                xx = x + dx[k]
                yy = y + dy[k]

                if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 1:
                    cnt += 1 
                        
            return cnt
        
        
        for i in range(m):
            for j in range(n):
                cnt = neibor(i, j)
                # print i, j, cnt
                if (board[i][j] == 1 and 2 <= cnt <= 3) or (board[i][j] == 0 and cnt == 3):
                        alivex.append(i)
                        alivey.append(j)
        
        alivecnt = 0
        for i in range(m):
            for j in range(n):
                board[i][j] = 0
                
                if alivecnt < len(alivex):
                    if alivex[alivecnt] == i and alivey[alivecnt] == j:
                        board[i][j] = 1
                        alivecnt += 1
                        
        return board
                    
                        
                        