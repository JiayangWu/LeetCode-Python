class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        from collections import defaultdict
        row2one_count = defaultdict(int)
        col2one_count = defaultdict(int)

        for row, col in indices:
            row2one_count[row] += 1
            col2one_count[col] += 1

        res = 0
        row_odd, col_odd = 0, 0
        for row in range(m):
            row_odd += row2one_count[row] % 2
        for col in range(n):
            col_odd += col2one_count[col] % 2
        return row_odd * (n - col_odd) + (m - row_odd) * col_odd