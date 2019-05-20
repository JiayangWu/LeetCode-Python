class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dpmax = [0 for _ in range(l)]
        dpmin = [0 for _ in range(l)]
        
        dpmax[0] = nums[0]
        dpmin[0] = nums[0]
        for i in range(1, l):
            dpmax[i] = max(nums[i], max(nums[i] * dpmax[i - 1], nums[i] * dpmin[i - 1]))
            dpmin[i] = min(nums[i], min(nums[i] * dpmax[i - 1], nums[i] * dpmin[i - 1]))

        return max(dpmax)