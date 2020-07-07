class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in nums]
        for i, x in enumerate(nums):
            dp[i] = max(x, dp[i - 1] + x) if i else x
        return max(dp)