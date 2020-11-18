class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        if not board or not board[0]:
            return None
        
        m, n = len(board), len(board[0])
        # 1. crush stage
        
        # flag all elements to be crushed
        todo = 0
        for i in range(m):
            for j in range(n - 2):
                if board[i][j] and abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                    todo = 1
                    
        for j in range(n):
            for i in range(m - 2):
                if board[i][j] and abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                    todo = 1
        # print board, todo
        # 2. gravity stage
        for j in range(n):
            lo, hi = m - 1, m - 1
            while hi >= 0:
                while hi >= 0 and board[hi][j] < 0:
                    hi -= 1
                
                if hi >= 0:
                    board[lo][j] = board[hi][j]
                    lo -= 1
                    hi -= 1
            
            while lo >= 0:
                board[lo][j] = 0
                lo -= 1

        # recursively call this function if more crush is necessary
        return self.candyCrush(board) if todo else board