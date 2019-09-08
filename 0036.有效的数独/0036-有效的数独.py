class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        row, column, squre  = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in squre[(i//3, j//3)]:
                        return False
                    else:
                        row[i].add(board[i][j])
                        column[j].add(board[i][j])
                        squre[(i//3, j //3)].add(board[i][j])
        return True
                