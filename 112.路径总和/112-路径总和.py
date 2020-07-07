# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.res = False
        
        def dfs(node, pathSum):
            if not self.res and node:
                pathSum += node.val
                
                if pathSum == s and not node.left and not node.right:
                    self.res = True
                    return
                
                dfs(node.left, pathSum)
                dfs(node.right, pathSum)
        dfs(root, 0)
        return self.res