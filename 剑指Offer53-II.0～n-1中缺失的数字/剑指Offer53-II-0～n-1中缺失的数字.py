class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num == len(nums):
                continue
            if num != i:
                nums[num], nums[i] = nums[i], nums[num]
                
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)