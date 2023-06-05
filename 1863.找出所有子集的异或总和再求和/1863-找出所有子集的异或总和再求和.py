class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]
        res = 0
        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subset = subset + [num]
                res += reduce(lambda x, y: x^y, new_subset)
                new_subsets.append(new_subset)
            subsets += new_subsets
        return res