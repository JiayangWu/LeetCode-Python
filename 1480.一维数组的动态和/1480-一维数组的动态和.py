class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 0
        res = []
        for num in nums:
            s += num
            res.append(s)
        return res