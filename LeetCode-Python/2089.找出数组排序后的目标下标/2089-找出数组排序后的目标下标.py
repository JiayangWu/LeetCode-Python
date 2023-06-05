class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num == target:
                res.append(i)
        return res