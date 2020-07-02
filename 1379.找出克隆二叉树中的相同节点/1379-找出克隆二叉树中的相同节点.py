# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        self.res = None
        def dfs(node1, node2):
            if not node1:
                return
            if node1 == target:
                self.res = node2
                return
            
            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)
                
        dfs(original, cloned)
        return self.res