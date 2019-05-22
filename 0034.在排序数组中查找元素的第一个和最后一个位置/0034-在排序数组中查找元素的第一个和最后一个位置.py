class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        #找第一个target
        while(lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo > hi: #不存在
            return [-1, -1]

        midtarget = mid
        lo, hi = 0, mid
        leftpos = 0
        while(lo <= hi):
            # print lo, hi
            if (hi >= 1 and nums[hi - 1] != target) or hi == 0: #找到左边界或者找到头了
                leftpos = hi
                break
            mid = (lo + hi) // 2
            if nums[mid] == target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1

        rightpos = 0
        lo, hi = midtarget, len(nums) - 1
        while(lo <= hi):
            if (lo <= len(nums) - 2 and nums[lo + 1] != target) or lo == len(nums) - 1: #找到右边界或者找到头了
                rightpos = lo
                break
            mid = (lo + hi + 1) // 2
            if nums[mid] == target:
                lo = mid 
            elif nums[mid] > target:
                hi = mid - 1
                
        return [leftpos, rightpos]
                