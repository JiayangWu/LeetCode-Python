class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        di = [1, 1, 1, -1, -1, -1, 0, 0]
        dj = [1, 0, -1, 1, 0, -1, 1, -1]

        if not board or not board[0]:
            return board

        m, n = len(board), len(board[0])
        dead_set = set()
        live_set = set()
        for i in range(m):
            for j in range(n):
                live_cell_count = 0
                for k in range(8):
                    ii, jj = i + di[k], j + dj[k]
                    if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 1:
                        live_cell_count += 1
                if board[i][j] == 1 and (live_cell_count < 2 or live_cell_count > 3):
                    dead_set.add((i, j))
                elif board[i][j] == 0 and live_cell_count == 3:
                    live_set.add((i, j))
        
        for i in range(m):
            for j in range(n):
                if (i, j) in dead_set:
                    board[i][j] = 0
                elif (i, j) in live_set:
                    board[i][j] = 1
        return board
        