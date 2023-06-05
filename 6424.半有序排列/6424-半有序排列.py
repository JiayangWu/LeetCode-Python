class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        index_1 = nums.index(1)
        index_n = nums.index(len(nums))
        if index_1 < index_n:
            return index_1 + (len(nums) - 1 - index_n)
        else:
            return index_1 + (len(nums) - 1 - index_n - 1)