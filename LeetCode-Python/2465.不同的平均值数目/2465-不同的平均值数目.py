class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        res = set()
        while nums:
            res.add((nums[0] + nums[-1]) / 2.0)
            nums = nums[1:-1]

        return len(res)