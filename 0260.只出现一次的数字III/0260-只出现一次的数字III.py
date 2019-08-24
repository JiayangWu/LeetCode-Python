class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b = 0, 0
        mask = 0
        for num in nums:
            mask ^= num
        mask = mask & (-mask)
        
        for num in nums:
            if mask & num:
                a ^= num
            else:
                b ^= num
        return [a, b]