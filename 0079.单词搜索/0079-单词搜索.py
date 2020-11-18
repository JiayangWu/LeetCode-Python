class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        self.res = False
        def dfs(word_idx, x0, y0):
            # print word_idx
            if word_idx >= len(word):
                self.res = True
                return 
            if not self.res:
                for k in range(len(dx)):
                    x1 = x0 + dx[k]
                    y1 = y0 + dy[k]

                    if 0 <= x1 < m and 0 <= y1 < n and board[x1][y1] == word[word_idx]:
                        temp = board[x1][y1]
                        board[x1][y1] = -1
                        dfs(word_idx + 1, x1, y1)
                        board[x1][y1] = temp
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = 0
                    dfs(1, i, j)
                    board[i][j] = temp
        return self.res