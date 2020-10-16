from collections import defaultdict
import copy
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[(i // 3, j // 3)].add(board[i][j])
        self.res = []
        def dfs(x, y):
            if x == 9 and y == 0:
                if self.isValidSudoku(board):
                    self.res = copy.deepcopy(board)
                return
            
            if not self.res:
                if board[x][y] != ".":
                    if y == 8:
                        dfs(x + 1, 0)
                    else:
                        dfs(x, y + 1)
                    return
                
                for num in range(1, 10):
                    num = str(num)
                    if num not in row[x] and num not in col[y] and num not in square[(x // 3, y // 3)]:
                        board[x][y] = num

                        row[x].add(num)
                        col[y].add(num)
                        square[(x // 3, y // 3)].add(num)
                        if y == 8:
                            dfs(x + 1, 0)
                        else:
                            dfs(x, y + 1)
                        board[x][y] = "."
                        row[x].remove(num)
                        col[y].remove(num)
                        square[(x // 3, y // 3)].remove(num)

        dfs(0, 0)
        board[:] = self.res


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[(i // 3, j // 3)]:
                        return False
                    else:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        square[(i // 3, j // 3)].add(board[i][j])
        return True