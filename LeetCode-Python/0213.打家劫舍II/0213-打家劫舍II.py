class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i][0/1] 0 represents room1 was safe
        n = len(nums)
        if len(nums) <= 2:
            return max(nums)
        dp = [[0, 0]for _ in range(n)]
        dp[0][1] = nums[0]
        dp[1][1] = nums[0]
        dp[1][0] = nums[1]
        for i in range(2, n):
            num = nums[i]
            if i != n - 1:
                dp[i][0] = max(dp[i - 2][0] + num, dp[i - 1][0])
                dp[i][1] = max(dp[i - 2][1] + num, dp[i - 1][1])
            else:
                dp[i][0] = max(dp[i - 2][0] + num, dp[i - 1][0])
                dp[i][1] = max(dp[i - 2][1], dp[i - 1][1])
        return max(dp[n - 1][0], dp[n - 1][1])