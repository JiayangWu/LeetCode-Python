class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []

        def dfs(l, r, tmp):
            if not l and not r:
                res.append(tmp[:])
            if l:
                dfs(l - 1, r, tmp + "(")
            if l < r:
                dfs(l, r - 1, tmp + ")")
        dfs(n, n, "")
        return res