
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, l = list(), len(nums)
        def dfs(n, tmp):
            if len(tmp) == l:
                res.append(tmp[:])
                return
            for i, x in enumerate(n):
                tmp.append(x)
                dfs(n[:i] + n[i + 1:], tmp)
                tmp.pop()
            
            
        for i, x in enumerate(nums):
            dfs(nums[:i] + nums[i + 1:], [x])
            
        return res