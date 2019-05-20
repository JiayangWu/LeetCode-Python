class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        m = len(board)
        if m == 0:
            return 0
        n = len(board[0])
        if n == 0:
            return 0
        res = 0    
        def dfs(x, y):
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                
                if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == "X":
                    board[xx][yy] = "."
                    dfs(xx, yy)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    # print 1
                    board[i][j] = "."
                    dfs(i, j)
                    res += 1
                    
        return res