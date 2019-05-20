class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = nums.index(max(nums))
        nums.sort()
        if len(nums) == 1:
            return 0
        if nums[-1] >= 2 * nums[-2]:
            return i
        return -1