# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp = root.right
        root.right = root.left
        root.left = None
        
        node = root
        while node.right:
            node = node.right
        node.right = tmp
        