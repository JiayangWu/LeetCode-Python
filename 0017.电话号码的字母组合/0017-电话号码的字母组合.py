class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
               
        res = []
        # for i, digit in enumerate(digits)
        def dfs(nums, tmp):
            if not nums:
                res.append(tmp)
                return
                   
            for char in mapping[int(nums[0])]:
                dfs(nums[1:], tmp + char)
                          
        dfs(digits, "")
        return res