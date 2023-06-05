class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:    
        col_grid = [list(col) for col in zip(*grid)]
        res = 0
        for row in grid:
            for col in col_grid:
                res += row == col
        return res