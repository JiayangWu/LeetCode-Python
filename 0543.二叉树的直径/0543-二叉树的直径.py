# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def Height(node):
            if not node:
                return 0
            return 1 + max(Height(node.left), Height(node.right))
        return max(self.diameterOfBinaryTree(root.left), Height(root.left) + Height(root.right), self.diameterOfBinaryTree(root.right))