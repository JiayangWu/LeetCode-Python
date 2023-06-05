class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        # validate row
        for i in range(9):
            row = [digit for digit in board[i] if digit.isdigit()]
            s = set(row)
            if len(s) < len(row):
                return False

        # validate col
        boardT = [list(col) for col in zip(*board)]
        for j in range(9):
            col = [digit for digit in boardT[j] if digit.isdigit()]
            s = set(col)
            if len(s) < len(col):
                return False

        # validate smaller 3 * 3 square
        rowcol2digitset = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in rowcol2digitset[str(i // 3) + str(j // 3)]:
                        return False
                    rowcol2digitset[str(i // 3) + str(j // 3)].add(board[i][j])

        return True