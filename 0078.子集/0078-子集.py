import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """     
        res, tmp = [], []
        
        def generate(nums, n):
            res.append(tmp[:])
            
            if n == len(nums):
                return 
            for i in range(n, len(nums)):
                tmp.append(nums[i])
                n += 1
                generate(nums, n)
                tmp.pop()
                
        generate(nums, 0)
        return res

        