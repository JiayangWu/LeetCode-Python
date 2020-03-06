# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, summ):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        
        def dfs(node, path, s):
            if not node:
                return
            
            if not node.left and not node.right:
                if s + node.val == summ:  
                    path.append(node.val)
                    self.res.append(path)
                return
            
            dfs(node.left, path + [node.val], s + node.val)
            dfs(node.right, path + [node.val], s + node.val)
           
        dfs(root, [], 0)
        return self.res