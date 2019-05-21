class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # sublist = []
        s = -99999
        res = -99999
        for i in range(len(nums) - k + 1):
            if s == -99999:
                s = sum(nums[:k])
            else:
                s -= nums[i - 1]
                s += nums[i + k - 1]
            # print sublist    
            res = max(res, s * 1.0 / k)
            
        return res
                
                
                