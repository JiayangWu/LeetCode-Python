class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = sum(nums)
        
        t = 0
        res = []
        for num in sorted(nums)[::-1]:
            res.append(num)
            t += num
            s -= num
            
            if t > s:
                return res