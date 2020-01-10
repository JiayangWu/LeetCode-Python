# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)

            self.res += abs(l) + abs(r)
            return l + r + node.val - 1
        dfs(root)
        return self.res