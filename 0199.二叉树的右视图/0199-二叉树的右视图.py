# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth > len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth +1)
            
            
        dfs(root, 1)
        return res