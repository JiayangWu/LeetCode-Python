class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0 for _ in nums]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    res[i] += 1
                    
        return res