class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n - 1) + f(n - 2)
        # dp[n] = dp[n -1] + dp[n - 2]
        # memo = dict()
        # def dfs(n):
        #     if n < 0:
        #         return 0
        #     if n <= 1:
        #         return 1
        #     if n in memo:
        #         return memo[n]
        #     res = dfs(n - 1) + dfs(n - 2)
        #     memo[n] = res
        #     return res
        # return dfs(n)
        f0, f1 = 1, 1
        for i in range(1, n):
            newf = f0 + f1
            f0 = f1
            f1 = newf
        return f1