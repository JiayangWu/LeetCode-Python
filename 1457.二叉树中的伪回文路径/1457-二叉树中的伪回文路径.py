# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def dfs(node, path):
            if not node:
                return
            
            path = path + [node.val]
            if not node.left and not node.right:
                if self.hasPalindromic(path):
                    self.res += 1
                
            dfs(node.left, path)
            dfs(node.right, path)
            
        dfs(root, [])
        return self.res
        
    def hasPalindromic(self, nums):
        from collections import Counter
        
        dic = Counter(nums)
        
        oddCnt = 0
        for val in dic.values():
            if val % 2:
                oddCnt += 1
                
        return oddCnt <= 1
        




