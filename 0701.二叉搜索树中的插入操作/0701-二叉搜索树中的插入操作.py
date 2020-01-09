# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        node, parent = root, root
        while node:
            parent = node
            node = parent.left if val < parent.val else parent.right
        if val > parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return root
# class Solution(object):
#     def insertIntoBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#         if not root:
#             return TreeNode(val)
#         if root.val > val:
#             root.left = self.insertIntoBST(root.left, val)
#         else:
#             root.right = self.insertIntoBST(root.right, val)
#         return root