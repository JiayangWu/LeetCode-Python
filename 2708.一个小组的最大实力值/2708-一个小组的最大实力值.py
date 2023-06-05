class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if all([num == 0 for num in nums]):
            return 0
        if len(nums) == 1:
            return nums[0]
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]

        res = 0
        neg_length = len(neg)
        if neg_length >= 2:
            if neg_length % 2 == 0:
                res = reduce((lambda x, y: x * y), neg)
            else:
                neg.sort()
                res = reduce((lambda x, y: x * y), neg[:-1])

        if pos:
            res = reduce((lambda x, y: x * y), pos) * max(res, 1)
        return res
