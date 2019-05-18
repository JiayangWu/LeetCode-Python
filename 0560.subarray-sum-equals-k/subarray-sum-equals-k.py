class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        pre_sum = 0
        record = defaultdict(int)
        record[0] = 1
        res = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            res += record[pre_sum - k]
            record[pre_sum] += 1
         
        return res