class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(tmp, nums):
            if not nums:
                res.append(tmp)
            
            for i, x in enumerate(nums):
                dfs(tmp + [x], nums[:i] + nums[i + 1:])
                
        dfs([], nums)
        return res