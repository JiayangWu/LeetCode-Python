class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) == len(nums):
            return len(nums) - 1
        zeroCnt = 0
        left = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCnt += 1
                while zeroCnt > 1:
                    if nums[left] == 0:
                        zeroCnt -= 1
                    left += 1
            res = max(res, right - left + 1 - zeroCnt)
        return res
                    