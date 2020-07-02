# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node, parent, grand):
            if not node:
                return
            if grand:
                self.res += node.val
            
            dfs(node.left, node.val % 2 == 0, parent)
            dfs(node.right, node.val % 2 == 0, parent)
        dfs(root, False, False)
        return self.res