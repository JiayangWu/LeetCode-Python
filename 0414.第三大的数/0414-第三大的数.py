class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) <= 2:
            return max(nums)
        
        maxx = max(nums)
        maxx2 = nums[0]
        for num in nums:
            if num == maxx:
                continue
            maxx2 = max(num, maxx2)
            
        res = nums[0]
        for num in nums:
            if num == maxx or num == maxx2:
                continue
            res = max(num, res)
        return res