class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        visited_rows, visited_cols = set(), set()
        res = 0
        for t, index, val in queries[::-1]:
            if t == 0:
                if index not in visited_rows:
                    res += val * (n - len(visited_cols))
                    visited_rows.add(index)
            elif t == 1:
                if index not in visited_cols:
                    res += val * (n - len(visited_rows))
                    visited_cols.add(index)

        return res

