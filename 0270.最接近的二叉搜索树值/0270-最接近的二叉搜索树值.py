# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)
        
        l = inOrder(root) 
        res = 0
        min_sub = float("inf")
        
        for num in l:
            if abs(num - target) < min_sub:
                min_sub = abs(num - target)
                res = num
        return res