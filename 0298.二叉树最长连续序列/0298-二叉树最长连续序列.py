# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        self.res = 1
        def dfs(node, tmp, parent_val):
            if not node:
                return 
            if node.val == parent_val + 1:
                tmp += 1
                self.res = max(self.res, tmp)
            else:
                tmp = 1
                
            dfs(node.left, tmp, node.val)
            dfs(node.right, tmp, node.val)
            
        dfs(root.left, 1, root.val)
        dfs(root.right, 1, root.val)
        
        return self.res
            