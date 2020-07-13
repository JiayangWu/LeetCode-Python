class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        nums.sort()
        # print nums
        # 1. 去前三个
        res = nums[-1] - nums[3]
        # 2. 去前两个和最后一个
        res = min(res, nums[-2] - nums[2])
        res = min(res, nums[-3] - nums[1])
        res = min(res, nums[-4] - nums[0])
        return res