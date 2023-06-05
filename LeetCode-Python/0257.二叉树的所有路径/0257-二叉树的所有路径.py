# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        self.res = []
        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))
            if not node.left and not node.right:
                self.res.append("->".join(path))

            dfs(node.left, path[:])
            dfs(node.right, path[:])

        dfs(root, [])
        return self.res