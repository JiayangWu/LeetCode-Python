# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # find the next node after p
        if not root:
            return None
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            return self.inorderSuccessor(root.left, p) or root 
            