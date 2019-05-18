class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        nums.sort()
        for index in range(0,len(nums)-1):
            if nums[index] == nums[index +1]:#or nums[index] == nums[index-1]:
                return True
        return False