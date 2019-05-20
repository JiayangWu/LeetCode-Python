class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        for index in range(l):
            if nums[index] >= target:
                return index
        return index + 1
            
        