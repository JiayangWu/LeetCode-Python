class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0 for _ in nums]

        prefix[0] = nums[0]
        min_s = min(0, nums[0])
        res = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
            res = max(prefix[i] - min_s, res)
            min_s = min(min_s, prefix[i])
        return res