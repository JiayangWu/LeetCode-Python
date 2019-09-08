class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lo, hi = 0, len(nums) - 1
        i = 0
        while i <= hi:
            x = nums[i]
            if x == 0:
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1
                i += 1
            elif x == 2:
                nums[hi], nums[i] = nums[i], nums[hi]
                hi -= 1
            else:
                i += 1
                