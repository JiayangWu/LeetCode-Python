class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #i 代表从nums结尾往前递增序列的头， j代表递增序列里比nums[i - 1]大的最小的元素
        
        l = len(nums)
        for i in range(l - 1, -1, -1):
            if nums[i - 1] < nums[i]:# 找到了需要的i
                break
        
        if i == 0: # 代表当前不存在下一个更大的序列，整体翻转即可
            nums[:] = nums[::-1]
            return nums
        
        for j in range(l - 1, i - 1, -1):
            if nums[j] > nums[i - 1]: #找到了需要的j
                break

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[i:][::-1]
        return nums