# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, cur_binary):
            if not node:
                return

            cur_binary = cur_binary * 2 + node.val
            if not node.left and not node.right:
                self.res += cur_binary
                return

            dfs(node.left, cur_binary)
            dfs(node.right, cur_binary)
        dfs(root, 0)
        return self.res