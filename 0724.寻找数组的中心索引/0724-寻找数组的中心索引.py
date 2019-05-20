class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lsum, rsum = 0, sum(nums)
        
        for index, item in enumerate(nums):
            rsum -= item
            
            if lsum == rsum:
                return index
            
            lsum += item
            
        
        return  -1