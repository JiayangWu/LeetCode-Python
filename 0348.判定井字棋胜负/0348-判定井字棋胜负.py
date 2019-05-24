class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.size = n
        self.board = [[0 for _ in range(n)] for j in range(n) ]
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row][col] = player
        if self.check(row, col, player):
            return player

        return 0
        
        
    def check(self, row, col, toe):
        row_valid = True
        col_valid = True
        
        
        for i in range(self.size):
            if self.board[row][i] != toe:
                row_valid = False
            if self.board[i][col] != toe:
                # print i, self.board[col][i], toe, col_valid
                col_valid = False
        
        if row != col and row + col != self.size - 1:
            return row_valid or col_valid
        
        dia_valid1 = False
        dia_valid2 = False
        if row == col:
            dia_valid1 = True
            for i in range(self.size):
                if self.board[i][i] != toe:
                    dia_valid1 = False
        if row + col == self.size - 1:
            dia_valid2 = True
            for i in range(self.size):
                if self.board[i][self.size - 1 - i] != toe:
                    dia_valid2 = False
        # print self.board
        # print (row, col), toe, row_valid, col_valid ,dia_valid1 ,dia_valid2
        return row_valid or col_valid or dia_valid1 or dia_valid2
        
        
        # for j in range(self.)
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)