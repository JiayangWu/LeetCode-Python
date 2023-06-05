class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, tmp):
            if left == 0 and right == 0:
                res.append(tmp)
                return
            if left > 0:
                dfs(left - 1, right, tmp + "(")
            if right > left:
                dfs(left, right - 1, tmp + ")")

        dfs(n, n, "")
        return res