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
        res = list()
        
        def dfs(node, tmp):
            if not node:
                return 
            
            tmp.append(node.val) 
            if not node.left and not node.right and sum(tmp) == s:
                res.append(tmp[:])
            
            dfs(node.left, tmp)
            dfs(node.right, tmp)
            tmp.pop()
            
        dfs(root, list())        
        return res