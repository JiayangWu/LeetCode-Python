# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.res = None
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            if not self.res and node.val > p.val:
                self.res = node
                return
            inorder(node.right)

        inorder(root)
        return self.res