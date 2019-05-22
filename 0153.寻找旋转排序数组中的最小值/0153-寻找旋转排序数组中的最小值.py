class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # m = len(nums) / 2
        b = 0
        e = len(nums)-1
        while(b < e):
            m = b + (e-b) / 2
            if nums[m] < nums[e]: 
                e = m
            else:
                b = m+1
        return nums[b]
                
            