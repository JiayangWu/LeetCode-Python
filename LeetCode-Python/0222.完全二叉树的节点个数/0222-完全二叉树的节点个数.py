# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return 0
            
            return 1 + inorder(node.left) + inorder(node.right)
        return inorder(root)