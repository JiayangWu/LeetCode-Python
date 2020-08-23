class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pre_sum = {0}
        res = 0
        s = 0
        for num in nums:
            s += num
            if s - target in pre_sum:
                res += 1
                s = 0
                pre_sum = {0}
            else:
                pre_sum.add(s)
        return res
