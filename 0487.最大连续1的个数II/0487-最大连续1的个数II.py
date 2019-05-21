class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        zero = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            while(zero > 1):
                if nums[left] == 0:
                    zero -= 1
                left += 1
            res = max(res, right - left + 1)
                
        return res
                
        