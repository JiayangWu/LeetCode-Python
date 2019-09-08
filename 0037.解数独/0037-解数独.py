class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        row, column, squre  = defaultdict(set), defaultdict(set), defaultdict(set)
        
        self.res = []
        def dfs(x, y):
            
            if x == 8 and y == 9:
                # print board
                for roww in board:
                    self.res.append(roww[:])
                # print self.res
                return
            if y == 9:
                dfs(x + 1, 0)
                return
            if board[x][y].isdigit():
                dfs(x, y + 1)
                return
                
            for k in range(1,10):
                if str(k) not in row[x] and str(k) not in column[y] and str(k) not in squre[(x // 3, y // 3)]:
                    board[x][y] = str(k)
                    row[x].add(str(k))
                    column[y].add(str(k))
                    squre[(x // 3, y // 3)].add(str(k))
                    
                    dfs(x, y + 1)
                    
                    board[x][y] = "."
                    row[x].remove(str(k))
                    column[y].remove(str(k))
                    squre[(x // 3, y // 3)].remove(str(k))
            
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    row[i].add(board[i][j].encode("utf-8"))
                    column[j].add(board[i][j].encode("utf-8"))
                    squre[(i // 3, j // 3)].add(board[i][j].encode("utf-8"))

        dfs(0, 0)
        board[:] = self.res