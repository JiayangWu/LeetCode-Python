# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        def dfs(node):
            if not node:
                return

            if node.left and not node.right:
                self.res.append(node.left.val)
            if node.right and not node.left:
                self.res.append(node.right.val)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res