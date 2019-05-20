class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not len(word):
            return False
        
        m, n = len(board), len(board[0])
        if len(word) > m *n:
            return False
        
        self.res = False
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = [[0 for _ in range(n + 1)] for j in range(m + 1)]
        
        def dfs(start, x0, y0):
            if start >= len(word) or board[x0][y0] != word[start]: #找不到解
                return
            
            visited[x0][y0] = 1
            if board[x0][y0] == word[start]:
                if start == len(word) - 1: #找到一个可行解啦！！！
                    self.res = True
                    return
                else:
                    for k in range(4):
                        x = x0 + dx[k]
                        y = y0 + dy[k]
                        
                        if 0<= x < m and 0<= y < n and visited[x][y] == 0  and not self.res: #not self.res很关键，剪枝非常重要
                            dfs(start + 1, x, y) #找下一个字母
            visited[x0][y0] = 0 #回溯
                            
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(0, i, j) #开始搜索
                if self.res:
                    return self.res
        return self.res
        
        
        
        