class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        b = 0
        r = 0
        w = 0
        for item in nums:
            if item == 0:
                r+= 1
            if item == 1:
                w += 1
            if item == 2:
                b += 1
        for index,item in enumerate(nums):
            if r!= 0:
                nums[index] = 0
                r -= 1
                continue
            if w!= 0:
                nums[index] = 1
                w -= 1
                continue
            if b!= 0:
                nums[index] = 2
                b -= 1
                continue
        # return nums
            
        