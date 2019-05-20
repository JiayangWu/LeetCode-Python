class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [nums[0]]
        res = dp[0]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
            if dp[-1] > res:
                res = dp[-1]
        return res