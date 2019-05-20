# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1, leaf2 = list(), list()
        
        def dfs(node, leaf):
            if not node:
                return
            if not node.left and not node.right:#leaf
                leaf.append(node.val)
                return
            
            dfs(node.left, leaf)
            dfs(node.right, leaf)
            
        
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        # print leaf
        return leaf1 == leaf2