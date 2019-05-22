class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        lo, hi = 0, len(nums) - 1
        while(lo <= hi):
            mid = (lo + hi) // 2
            # print mid, nums[mid]
            if mid + 1 < len(nums) and nums[mid] > nums[mid +1]:
                break
            if nums[mid] < nums[-1]:
                hi = mid - 1
            elif nums[mid] >= nums[0]:
                lo = mid + 1
                
        if lo > hi:#Ã»ÓĞĞı×ª
            lo, hi = 0, len(nums) - 1
        else:
            if target >= nums[0]:
                lo, hi = 0, mid
            else:
                lo, hi = mid + 1, len(nums) - 1

        while(lo <= hi):
            # print lo, hi
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1
                