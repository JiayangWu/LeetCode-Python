class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        row, column, squre  = defaultdict(set), defaultdict(set), defaultdict(set)
        fill_list = []
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit(): #ÅÅ³ýµô¿ÕµÄÇé¿ö
                    row[i].add(board[i][j].encode("utf-8"))
                    column[j].add(board[i][j].encode("utf-8"))
                    squre[(i // 3, j // 3)].add(board[i][j].encode("utf-8"))
                else:
                    fill_list.append([i, j])
                    
        self.result = []           
        def backtrack(idx):
            if idx == len(fill_list):
                for row1 in board:
                    self.result.append(row1[:])
                return
            if not self.result:
                i, j = fill_list[idx][0], fill_list[idx][1]
                for digit in range(1, 10):
                    if str(digit) in row[i] or str(digit) in column[j] or str(digit) in squre[(i // 3, j // 3)]:
                        continue

                    board[i][j] = str(digit)
                    row[i].add(board[i][j])
                    column[j].add(board[i][j])
                    squre[(i // 3, j // 3)].add(board[i][j])

                    backtrack(idx + 1)

                    row[i].remove(board[i][j])
                    column[j].remove(board[i][j])
                    squre[(i // 3, j // 3)].remove(board[i][j])

        backtrack(0)  
        for i in range(9):
            for j in range(9):
                board[i][j] = self.result[i][j]
