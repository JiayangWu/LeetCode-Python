class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res = []

        for i, num in enumerate(nums):
            pre_count = len(set(nums[:i + 1]))
            post_count = len(set(nums[i + 1:]))

            res.append(pre_count - post_count)
        return res