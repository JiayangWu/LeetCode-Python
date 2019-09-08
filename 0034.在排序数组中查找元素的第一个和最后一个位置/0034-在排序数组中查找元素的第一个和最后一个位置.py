class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            
            mid = (lo + hi) // 2
            # print lo, hi, mid, nums
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        if lo > hi:
            return [-1, -1]
        midposition = mid
        leftside, rightside = midposition, midposition
        #урвС╠ъ╫Г
        # print 1
        lo, hi = 0, midposition
        while lo <= hi:
            # print lo, hi, mid
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                if mid == 0 or (mid - 1 >= 0 and nums[mid - 1] < target):
                    leftside = mid
                    break
                else:
                    hi = mid - 1
        # print 1      
        #урср╠ъ╫Г
        lo, hi = midposition, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] == target:
                if mid == len(nums) - 1 or (mid + 1 < len(nums) and nums[mid + 1] > target):
                    rightside = mid
                    break
                else:
                    lo = mid + 1
        
        return [leftside, rightside]
                    
                
            