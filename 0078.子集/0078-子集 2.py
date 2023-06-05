class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            tmp = res[:]
            for item in res:
                tmp.append(item + [num])     
            res = tmp[:]
            
        return res