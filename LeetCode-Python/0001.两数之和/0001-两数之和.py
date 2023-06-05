class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value2index = {}

        for index, num in enumerate(nums):
            if target - num in value2index:
                return [value2index[target - num], index]
            value2index[num] = index
        