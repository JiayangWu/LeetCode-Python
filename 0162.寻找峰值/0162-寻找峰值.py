class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
          
        if len(nums) <= 1:
            return 0
        lo, hi = 0, len(nums) - 1
        while(lo < hi):
            # print lo,hi
            mid = lo + (hi - lo) / 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return lo