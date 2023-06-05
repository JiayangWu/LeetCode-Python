# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = not root.left or (self.isUnivalTree(root.left) and root.left.val == root.val)
        right = not root.right or (self.isUnivalTree(root.right) and root.right.val == root.val)
        return left and right 