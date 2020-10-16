class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        dic = {} # key is prefix_sum and val is the smallest idx
        dic[0] = -1
        res = 0
        for i, num in enumerate(nums):
            if i > 0:
                nums[i] += nums[i - 1]
            if nums[i] not in dic:
                dic[nums[i]] = i
            target = nums[i] - k
            # print(dic, nums[i])
            if target in dic:
                res = max(res, i - dic[target])

        return res