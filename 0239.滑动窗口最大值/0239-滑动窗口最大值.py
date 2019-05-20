class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        window, res = list(), list()
        for i, x in enumerate(nums):
            
            if window and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] < x:
                
                window.pop()
                
            window.append(i)
            
            if i >= k - 1:
                res.append(nums[window[0]])
                
        return res
        
