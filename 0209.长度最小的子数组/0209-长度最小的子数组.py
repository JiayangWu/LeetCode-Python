class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = len(nums) + 1
        lo, hi = 0, -1
        subsum = 0
        while(lo < len(nums)):
           
            if subsum < s and hi + 1 < len(nums):
                hi += 1
                subsum += nums[hi]                
            else:                
                subsum -= nums[lo]
                lo += 1
                
            if subsum >= s:
                res = min(res, hi - lo + 1)
                
        return res if res != len(nums) + 1 else 0
            
        
        