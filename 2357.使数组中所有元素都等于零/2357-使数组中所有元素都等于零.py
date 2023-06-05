class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        while sum(nums):
            res += 1
            m = 101
            for num in nums:
                if num:
                    m = min(m, num)
            for i, num in enumerate(nums):
                if num:
                    nums[i] -= m
        return res