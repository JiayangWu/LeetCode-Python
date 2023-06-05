class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # f(i) = f(i - zero) + f(i - one) 
        # 00, 10, 11, 10, 0, 1
        # self.res = 0
        # MOD = int(1e9 + 7)
        # memo = dict()
        # def dfs(i):
        #     if i == 0:
        #         return 1
        #     count = 0
        #     if i in memo:
        #         return memo[i]
        #     if i >= zero:
        #         count += dfs(i - zero)
        #     if i >= one:
        #         count += dfs(i - one)
        #     # l represents count of distinct good string of length i
        #     if i >= low:
        #         self.res += count % MOD
        #     memo[i] = count
        #     return count
        # dfs(high)
        # return self.res % MOD
        MOD = int(1e9 + 7)
        dp = [0] * (high + max(zero, one))
        dp[0] = 1
        res = 0
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            if i >= low:
                res += dp[i] % MOD
        return res % MOD