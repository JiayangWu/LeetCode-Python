class Solution:
    def countAsterisks(self, s: str) -> int:
        bar = False
        res = 0
        for char in s:
            if char ==  "|":
                bar = not bar
            if not bar and char == "*":
                res += 1
        return res