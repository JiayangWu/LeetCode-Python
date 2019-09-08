# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        def getHeight(node, h):
            if not node:
                return h
            return max(getHeight(node.left, h + 1), getHeight(node.right, h + 1))
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(getHeight(root.left, 0) - getHeight(root.right, 0)) <= 1