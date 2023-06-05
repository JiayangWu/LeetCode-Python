# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.res = 0
        def inorder(node):
            if not node:
                return

            inorder(node.right)
            self.count += 1
            if self.count == k:
                self.res = node.val
            
            inorder(node.left)
            
        inorder(root)
        return self.res