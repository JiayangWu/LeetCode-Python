class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i]:
                dp.append(dp[i-1] + 1)
            else:
                dp.append(0)
        # print dp
        return max(dp)