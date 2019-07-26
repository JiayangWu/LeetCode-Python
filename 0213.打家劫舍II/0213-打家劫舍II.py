class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.rob2(nums[1:]), self.rob2(nums[:-1]))
    
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return 0
        if not nums:
            return 0
        dp = [0 for _ in nums]
        dp[0] = nums[0] 
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(dp[0], nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]