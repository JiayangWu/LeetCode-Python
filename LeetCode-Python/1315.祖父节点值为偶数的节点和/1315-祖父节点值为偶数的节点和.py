# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        def dfs(node, isParentEven, isGrandparentEven):
            if not node:
                return

            if isGrandparentEven:
                self.sum += node.val

            dfs(node.left, node.val % 2 == 0, isParentEven)
            dfs(node.right, node.val % 2 == 0, isParentEven)

        dfs(root, False, False)
        return self.sum