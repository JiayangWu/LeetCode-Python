# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def dfs(node):
            if not node:
                return 
 
            if node.left:
                dfs(node.left)
                node.val += node.left.val - 1
            if node.right:
                dfs(node.right)
                node.val += node.right.val - 1
                
            self.res += abs(node.val - 1)
            
            
        dfs(root)
        return self.res