class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        res = 0
        for ch in s:
            if ch == "(":
                depth += 1
                res = max(res, depth)
            elif ch == ")":
                depth -= 1

        return res