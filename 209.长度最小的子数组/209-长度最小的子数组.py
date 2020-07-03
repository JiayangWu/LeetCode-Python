class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        window_sum = 0
        res = len(nums)
        for right in range(len(nums)):
            window_sum += nums[right]
            
            while window_sum >= s:
                res = min(res, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return res if sum(nums) >= s else 0