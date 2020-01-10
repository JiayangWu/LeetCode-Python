# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = not root.left or (self.isUnivalTree(root.left) and root.val == root.left.val)
        right = not root.right or (self.isUnivalTree(root.right) and root.val == root.right.val)
        return left and right