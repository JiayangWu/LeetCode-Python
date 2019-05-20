class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        for i, x in enumerate(nums):
            p = abs(x)
            # print nums, p
            if nums[p - 1] < 0: #说明p重复了
                res.append(p)
            else:
                nums[p - 1] *= -1
                
        return res