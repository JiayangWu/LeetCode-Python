class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_res = []
            for subset in res:
                new_res.append(subset + [num])
            res += new_res
        return res