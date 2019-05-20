class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 对于处于1~n之间的数，把它们放到nums[i - 1]的位置上
        
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
        for i, x in enumerate(nums):
            if x != i + 1:
                return i + 1
        
        return len(nums) + 1