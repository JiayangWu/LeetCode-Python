class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            for node in row:
                if node < 0:
                    res += 1
        return res