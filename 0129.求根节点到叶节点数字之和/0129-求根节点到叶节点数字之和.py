# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, cur_sum):
            if not node:
                return

            cur_sum = cur_sum * 10 + node.val
            if not node.left and not node.right:
                self.res += cur_sum
            else:
                dfs(node.left, cur_sum)
                dfs(node.right, cur_sum)

        dfs(root, 0)
        return self.res