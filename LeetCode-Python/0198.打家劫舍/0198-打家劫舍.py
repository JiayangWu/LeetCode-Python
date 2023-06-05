class Solution:
    def rob(self, nums: List[int]) -> int:
        # res = 0
        # n = len(nums)
        # memo = dict()
        # def dfs(n):
        #     if n < 0:
        #         return 0
        #     if n in memo:
        #         return memo[n]
        #     # f(n) = max(f(n - 1), f(n - 2) + nums[n])
        #     res = max(dfs(n - 1), dfs(n - 2) + nums[n])
        #     memo[n] = res
        #     return res
        # return dfs(n - 1)
        res = 0
        n = len(nums)
        # dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])
        # dp[n + 2] = max(dp[n + 1], dp[n] + nums[n])
        # f(2) = max(f1, f0 + nums[n])
        f0, f1 = 0, 0
        for i, num in enumerate(nums):
            new_f = max(f1, f0 + num)
            f0 = f1
            f1 = new_f
        return f1