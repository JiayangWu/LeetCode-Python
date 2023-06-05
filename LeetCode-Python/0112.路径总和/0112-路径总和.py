# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        def dfs(node, path_sum):
            if not node:
                return 

            path_sum += node.val
            if targetSum == path_sum and (not node.left and not node.right):
                self.res = True
            
            if not self.res:
                dfs(node.left, path_sum)
                dfs(node.right, path_sum)
        
        dfs(root, 0)
        return self.res