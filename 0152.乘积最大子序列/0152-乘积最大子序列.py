class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp[i] = max(nums[i], nums[i] * dp[i - 1])
        
        dp = [0 for i in nums]
        dpmin = [0 for i in nums]
        
        dp[0], dpmin[0] = nums[0], nums[0]
        for i, num in enumerate(nums):
            if i > 0:
                dp[i] = max(num, max(dp[i - 1] * num, dpmin[i - 1] * num))
                dpmin[i] = min(num, min(dp[i - 1] * num, dpmin[i - 1] * num))
        
        # print dp
        return max(dp)