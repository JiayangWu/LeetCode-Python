class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, x in enumerate(index):
            res = res[:x] + [nums[i]] + res[x:]
        return res