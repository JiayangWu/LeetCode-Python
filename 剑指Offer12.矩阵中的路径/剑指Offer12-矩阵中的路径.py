class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m, n = len(board), len(board[0])

        self.res = False 
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        def dfs(x0, y0, start):
            if start == len(word) - 1 or self.res:
                self.res = True 
                return 

            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k] 

                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] == word[start + 1]:
                    visited.add((x, y))
                    dfs(x, y, start + 1)
                    visited.remove((x, y))
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set([(i, j)])
                    dfs(i, j, 0)
        return self.res