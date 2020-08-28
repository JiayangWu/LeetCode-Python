class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res += bin(num).count("1")

        res += len(bin(max(nums))[2:]) - 1
        return res