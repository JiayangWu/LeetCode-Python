class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        
        for i, x in enumerate(nums):
            p = abs(x)
            if nums[p - 1] > 0:
                nums[p - 1] *= -1
        # print nums
        return [i + 1 for i, x in enumerate(nums) if x > 0]