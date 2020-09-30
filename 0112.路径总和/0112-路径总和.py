# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(node, s):
            if not node:
                return False

            s += node.val
            if not node.left and not node.right:
                return s == sum
            return dfs(node.left, s) or dfs(node.right, s)

        return dfs(root, 0)