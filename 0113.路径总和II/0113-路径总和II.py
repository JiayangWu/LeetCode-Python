# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(node, path, s):
            if not node:
                return []
            s += node.val
            if not node.left and not node.right:
                if s == sum:
                    res.append(path + [node.val])
            
            dfs(node.left, path + [node.val], s)
            dfs(node.right, path + [node.val], s)

        dfs(root, [], 0)
        return res