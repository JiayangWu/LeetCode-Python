class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for index,item in enumerate(nums):
            if item != 0:
                continue
            else:
                for index0 in range(index+1,l):
                    if nums[index0] != 0:
                        print nums[index], nums[index0]
                        nums[index], nums[index0] = nums[index0], nums[index]
                        break