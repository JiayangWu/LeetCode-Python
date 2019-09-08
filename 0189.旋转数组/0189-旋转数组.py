class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #每次把最后一个数放到最前面，放k次
        for i in range(k):
            # tmp = nums[0]
            tmp = nums.pop()
            nums.insert(0, tmp)
        