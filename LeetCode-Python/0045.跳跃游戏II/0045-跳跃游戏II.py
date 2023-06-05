class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for _  in nums]
        dp[0] = 0
        for i, num in enumerate(nums):
            for j in range(1, 1 + num):
                if i + j < len(nums):
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]