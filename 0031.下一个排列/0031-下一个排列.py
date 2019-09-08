class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums
        # print nums, sorted(nums)[::-1]
        if nums == sorted(nums)[::-1]:
            nums[:] = nums[::-1]
            return
        
        i = len(nums) - 1
        while(i - 1 >= 0 and nums[i - 1] >= nums[i]):
            i -= 1
        i -= 1    
        tmp = nums[i]
        j = len(nums) - 1
        while(j >= i and nums[j] <= tmp):
            j -= 1
            if nums[j] > tmp:
                break

        # print tmp, nums[j], nums[i]
        nums[i], nums[j] = nums[j], nums[i]
        # print nums
        nums[i+ 1:] = nums[i + 1:][::-1]
        return 
        