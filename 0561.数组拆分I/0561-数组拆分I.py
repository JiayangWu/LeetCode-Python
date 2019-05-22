class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums),2)) 