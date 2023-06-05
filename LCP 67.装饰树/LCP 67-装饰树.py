# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return node

            left, right = node.left, node.right
            if left:
                node.left = TreeNode(-1, left)

            if right:
                node.right = TreeNode(-1, None, right)

            dfs(left)
            dfs(right)
            return node 

        return dfs(root)
            