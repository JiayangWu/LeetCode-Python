class Solution(object):
    def canDivideIntoSubsequences(self, nums, K):
        """
        :type nums: List[int]
        :type K: int
        :rtype: bool
        """
        if len(nums) < K:
            return False
        from collections import Counter
        d = Counter(nums)
        maxx = 1
        for key, val in d.items():
            maxx = max(val, maxx)
            
        return maxx * K <= len(nums)