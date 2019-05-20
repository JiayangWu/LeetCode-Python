class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        res = [1] * l
        for i in range(1,l):
            res[i] = res[i - 1] *nums[i - 1]
        
        p = 1
        for i in reversed(range(l)):
            res[i] *= p
            p *= nums[i]
            
        return res
                
        