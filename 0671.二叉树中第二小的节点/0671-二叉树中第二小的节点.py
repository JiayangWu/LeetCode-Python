# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        res = []
        def dfs(node):
            if not node:
                return
            
            if node.val != root.val:
                res.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        res.sort()
        return -1 if len(res) == 0 else res[0]