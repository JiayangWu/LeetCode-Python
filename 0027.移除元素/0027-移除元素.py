class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        for i, num in enumerate(nums):
            if num == val:
                j = i + 1
                while(j < len(nums) and nums[j] == num):
                    j += 1
                t = j
                while(j < len(nums)):
                    nums[i] = nums[j]
                    i += 1
                    j += 1
                return i
                
                    