# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(node, path):
            if not node:
                return
            
            path += [node.val]
            if not node.left and not node.right and sum(path) == s:
                res.append(path[:])
                
            dfs(node.left, path)
            dfs(node.right, path)
            
            path.pop()
            
        dfs(root, [])
        return res