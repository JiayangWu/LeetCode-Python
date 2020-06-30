class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        MOD = 10 ** 9 + 7
        while left <= right:
            s = nums[left] + nums[right]
            l = right - left
            if s <= target:
                res = (res + (1 << l)) % MOD
                left += 1
            else:
                right -= 1
        return res