class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            if i == num:
                return i  
        return -1