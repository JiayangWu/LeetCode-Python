class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = 1 + dp[i - 1]
            res = max(dp[i], res)
                
        return res
                
                