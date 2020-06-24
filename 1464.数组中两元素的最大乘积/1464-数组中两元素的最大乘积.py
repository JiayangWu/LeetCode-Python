class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = sorted(nums)
        return (l[-1] - 1) * (l[-2] - 1)