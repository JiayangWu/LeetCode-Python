class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = collections.Counter(nums)
        
        res = list()
        for key, val in dic.items():
            if val == 1:
                res.append(key)
                
        return res