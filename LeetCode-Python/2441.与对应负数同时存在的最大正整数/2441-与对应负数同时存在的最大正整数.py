class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        res = -1
        for num in nums:
            if -num in s:
                res = max(num, -num, res)
        return res