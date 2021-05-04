class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0 
        res = 0
        for i, num in enumerate(nums):
            if i:
                if num <= nums[i - 1]:
                    res += (nums[i - 1] + 1) - num
                    nums[i] = nums[i - 1] + 1
            # print(nums)
        return res
                