# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = float("inf")

        def dfs(node, cur_depth):
            if not node:
                return
            cur_depth += 1
            if not node.left and not node.right:
                self.res = min(cur_depth, self.res)
            dfs(node.left, cur_depth)
            dfs(node.right, cur_depth)

        dfs(root, 0)
        return self.res

        
            