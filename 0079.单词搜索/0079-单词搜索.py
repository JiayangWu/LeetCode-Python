class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        if not word:
            return True
        
        self.res = False
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        def dfs(start, x0, y0):
            if start == len(word) - 1:
                self.res = True
                return
            visited.add((x0, y0))
            
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                # print x, y
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] == word[start + 1] and not self.res:
                    visited.add((x, y))
                    dfs(start + 1, x, y)
                    visited.remove((x, y))
            
        m, n = len(board), len(board[0])
        # print m * n, len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    dfs(0, i, j)
                    if self.res:
                        return True
        return False