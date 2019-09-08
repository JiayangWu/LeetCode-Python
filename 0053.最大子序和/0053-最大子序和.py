class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [] # dp[i]表示以i结尾的连续子数组的最大和
        for i, x in enumerate(nums):
            if i == 0:
                dp.append(x)
            else:
                if dp[-1] < 0:
                    dp.append(x)
                else:
                    dp.append(dp[-1] + x)
                    
        return max(dp)