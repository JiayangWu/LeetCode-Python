class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = ["." * n for _ in range(n)]

        res = []
        def checkRowAndCol(row, col):
            for i in range(n):
                if (board[row][i] == "Q" and i != col) or (board[i][col] == "Q" and i != row): #发生了横向或者纵向冲突
                    return False
            return True
        
        def checkDoubleDio(row, col):
            add = row + col
            sub = col - row
            
            for x in range(n):
                if x == row: #跳过自身这个点
                    continue
                y = add - x
                # print add,sub, x, y
                if y >= 0 and y < n and x >= 0 and x < n and board[x][y] == "Q": #发生/冲突
                    return False
            
                y = sub + x
                if y >= 0 and y < n and x >= 0 and x < n and board[x][y] == "Q": #发生\冲突
                    return False
                
            return True
        
        
        def dfs(row, col):
            if col >= n: #本行所有位置都找完了
                return
            board[row] = "." * col + "Q" + (n - col - 1) * "." #把皇后放在(row, col)的位置上
            if checkRowAndCol(row, col) and checkDoubleDio(row, col): #如果没有发生冲突
                if row == n - 1: #如果放下的是最后一个皇后
                    # print board
                    res.append(board[:]) #找到一个可行解啦！！！
                else:
                    for i in range(n): #还要放更多的皇后，往下一行放吧
                        dfs(row + 1, i)
                        
            board[row] = "." * n #回溯，把本行放下的皇后拿回来
            # dfs(row, col + 1)
            return

        for i in range(n):
            dfs(0, i)
            
        return res