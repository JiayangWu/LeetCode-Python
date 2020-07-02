class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            
            if s == target:
                return [nums[left], nums[right]]
            elif s > target:
                right -= 1
            else:
                left += 1