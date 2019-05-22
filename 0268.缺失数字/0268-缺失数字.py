class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        idealsum = l*(l+1) /2
        realsum = sum(nums)
        return idealsum - realsum