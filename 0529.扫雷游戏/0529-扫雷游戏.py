class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board or not board[0]:
            return board
        
        m, n = len(board), len(board[0])
        visited = [[0 for _ in range(n + 1)] for j in range(m + 1)]
        
        x, y = click[0], click[1]
        if board[x][y] == "M":#一下就挖到地雷，可以直接修改然后返回
            board[x][y] = "X"
            return board
        
        dx = [1, 1, -1, -1, 0, 0, -1, 1]
        dy = [1, 0, -1, 0, 1, -1, 1, -1]
        
        def dfs(x0, y0):
            if board[x0][y0] == "M" or visited[x0][y0] == 1: #如果该点是地雷，或者已经来过了，就直接跑路
                return
                                               
            visited[x0][y0] = 1 #标记一下来过了
            mineCnt = 0         #统计当前点附近有几个地雷
            for k in range(8):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and board[x][y] == "M":
                    mineCnt += 1
            
            if mineCnt > 0:
                board[x0][y0] = str(mineCnt) #如果有雷，就直接说有几个雷
            else:
                board[x0][y0] = 'B' #没有相邻地雷，就还需要递归周围的点

                for k in range(8):
                    x = x0 + dx[k]
                    y = y0 + dy[k]

                    if 0 <= x < m and 0 <= y < n and visited[x][y] == 0:
                        dfs(x, y)

        dfs(x, y)
        return board