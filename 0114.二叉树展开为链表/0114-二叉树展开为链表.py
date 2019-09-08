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
            return None
        if not root.left and not root.right:
            return root
        
        self.flatten(root.left)
        self.flatten(root.right)
        ltree, rtree = root.left, root.right
        root.right = ltree
        root.left = None
        p = root
        while p.right:
            p = p.right
        p.right = rtree