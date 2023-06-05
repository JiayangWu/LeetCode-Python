class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = []
        for i, _ in enumerate(s):
            j = i
            cur_row, cur_col = startPos[0], startPos[1]
            while 1:
                if j == len(s):
                    break
                ins = s[j]
                if ins == "R":
                    cur_col += 1
                elif ins == "L":
                    cur_col -= 1
                elif ins == "U":
                    cur_row -= 1
                elif ins == "D":
                    cur_row += 1
                j += 1
                if self.moveOutside(cur_row, cur_col, n):
                    j -= 1
                    break
            res.append(j - i)
        return res

    def moveOutside(self, cur_row, cur_col, n):
        return not 0 <= cur_row < n or not 0 <= cur_col < n
