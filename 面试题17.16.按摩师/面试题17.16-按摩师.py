class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in nums]

        for i in range(len(nums)):
            dp[i] = nums[i]
            for j in range(i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return max(dp) if nums else 0