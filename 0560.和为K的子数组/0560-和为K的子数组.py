class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefix[i] = sum(nums[:i])
        # prefix[j] - prefix[i] = sum(nums[i:j])
        from collections import defaultdict
        
        prefix = [0 for _ in range(len(nums) + 1)]
        
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x
        
        dic = defaultdict(int)
        res = 0
        for i, x in enumerate(prefix):
            res += dic[x - k]
            dic[x] += 1
            
        return res