class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #从四条边的O往里找相邻的O染色成P，到不了的O变成X， P染色回O
        
        if not board or not board[0]:
            return board
        
        m, n = len(board), len(board[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        def dfs(x0, y0):
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    board[x][y] = "P"
                    dfs(x, y)
        
        
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "P"
                    dfs(i, j)
                    
        for j in [0, n - 1]:
            for i in range(m):
                 if board[i][j] == "O":
                    board[i][j] = "P"
                    dfs(i, j)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "P":
                    board[i][j] = "O"
                    