class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return self.triangularSum([nums[i] + nums[i - 1] for i in range(1, len(nums))]) % 10