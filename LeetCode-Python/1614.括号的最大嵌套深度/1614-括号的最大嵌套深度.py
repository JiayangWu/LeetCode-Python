class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cur_depth = 0
        for char in s:
            if char == "(":
                cur_depth += 1
                res = max(res, cur_depth)
            elif char == ")":
                cur_depth -= 1

        return res