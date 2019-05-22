class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for i in nums:
            r ^= i
        return r
           
        
       