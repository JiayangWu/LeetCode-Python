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
        self.res = 0
        def height(node):
            if not node:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)
            
            self.res = max(self.res, left_h + right_h) 
            return 1 + max(left_h, right_h)
        height(root)
        return self.res