class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start, end = 0, 0
        
        while start <= end and end < len(nums):
            end = max(end, start + nums[start])
            start += 1
        return end >= len(nums) - 1