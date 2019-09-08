class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        record = dict()
        def dfs(tmp, nums):
            if not nums:
                res.append(tmp)
                    
            for i, x in enumerate(nums):
                if i == 0 or nums[i] != nums[i - 1]:
                    dfs(tmp + [x], nums[:i] + nums[i + 1:])
                
        dfs([], nums)
        return res