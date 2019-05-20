class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        board = ["." * n for _ in range(n)]
        # print board
        self.res = 0
        def checkRowAndCol(row, col):
            for i in range(n):
                if (board[row][i] == "Q" and i != col) or (board[i][col] == "Q" and i != row):
                    return False
            return True
        
        def checkDoubleDio(row, col):
            add = row + col
            sub = col - row
            
            for x in range(n):
                if x == row:
                    continue
                y = add - x
                # print add,sub, x, y
                if y >= 0 and y < n and x >= 0 and x < n and board[x][y] == "Q":
                    return False
            
                y = sub + x
                if y >= 0 and y < n and x >= 0 and x < n and board[x][y] == "Q":
                    return False
                
            return True
        
        
        def dfs(row, col):
            if col >= n:
                return
            board[row] = "." * col + "Q" + (n - col - 1) * "."
            if checkRowAndCol(row, col) and checkDoubleDio(row, col):
                if row == n - 1:
                    # print board
                    self.res += 1
                else:
                    for i in range(n):
                        dfs(row + 1, i)
                        
            board[row] = "." * n
            # dfs(row, col + 1)
            return

        for i in range(n):
            dfs(0, i)
            
        return self.res