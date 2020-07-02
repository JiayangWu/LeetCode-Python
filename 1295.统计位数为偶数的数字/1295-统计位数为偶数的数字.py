class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                res += 1
        return res