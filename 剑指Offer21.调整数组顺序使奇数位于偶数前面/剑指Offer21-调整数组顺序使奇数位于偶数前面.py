class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1

        while left < right:
            if not nums[left] % 2 and nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2:
                left += 1
            if not nums[right] % 2:
                right -= 1
        return nums