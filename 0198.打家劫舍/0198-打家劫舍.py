class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [nums[0]]
        if len(nums) == 1:
            return dp[0]
        dp.append(max(nums[0], nums[1]))
        # if len(nums) == 2:
        #     return dp[1]
        for i in range(2, len(nums)):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))
        # print dp
        return dp[-1]