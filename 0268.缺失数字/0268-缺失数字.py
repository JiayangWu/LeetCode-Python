class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        for num in range(len(nums)):
            if num not in s:
                return num
        return len(nums)