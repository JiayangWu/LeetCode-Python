class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # res = 0
        # @cache
        # def dfs(n):
        #     # dfs(n) represents the cost to climb to index n
        #     if n < 0:
        #         return 0
        #     if n <= 1:
        #         return 0
        #     res = min(dfs(n - 1) + cost[n - 1], dfs(n - 2) + cost[n - 2])
        #     return res
        # return dfs(n)
        n = len(cost)
        res = 0
        f0, f1 = 0, 0
        for i in range(n - 1):
            new_f = min(f1 + cost[i + 1], f0 + cost[i])
            f0, f1 = f1, new_f
        return f1