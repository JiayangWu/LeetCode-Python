# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left and root.right:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            if root.left:
                return 1 + self.minDepth(root.left)
            if root.right:
                return 1 + self.minDepth(root.right)
            else:
                return 1
        else:
            return 0
        
        