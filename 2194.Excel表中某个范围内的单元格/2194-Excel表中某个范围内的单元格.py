class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        start_row, end_row = int(s[1]), int(s[-1])
        start_col, end_col = s[0], s[3]

        for cur in range(ord(start_col), ord(end_col) + 1):
            for row in range(start_row, end_row + 1):
                res.append(chr(cur) + str(row))
        return res