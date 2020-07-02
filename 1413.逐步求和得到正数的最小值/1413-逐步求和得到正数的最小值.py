class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_s = nums[0]
        s = 0 
        for num in nums:
            s += num 
            min_s = min(min_s, s)

        return 1 if min_s >= 1 else 1 - min_s