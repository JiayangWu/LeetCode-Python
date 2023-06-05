# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        left = root.left
        right = root.right
        
        self.flatten(left)
        root.right = left
        root.left = None
        
        p = root
        while p.right:
            p = p.right

        self.flatten(right)
        p.right = right

