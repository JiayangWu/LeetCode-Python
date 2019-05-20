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
        
        def dfs(node, tmp):
            if not node:
                return 
            
            tmp.append(node.val)
            if not node.left and not node.right and sum(tmp) == s:
                self.res = True
            
            dfs(node.left, tmp)
            dfs(node.right, tmp)
            tmp.pop()
        
        
        dfs(root, list())
        return self.res
            
        