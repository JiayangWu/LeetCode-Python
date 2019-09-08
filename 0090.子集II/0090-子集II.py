class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            tmp = res[:]
            for item in res:
                newitem = sorted(item + [num])
                if newitem not in tmp:
                    tmp.append(newitem)
            res = tmp[:]
            
        return res