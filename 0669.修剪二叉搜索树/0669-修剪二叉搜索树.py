# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None 

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        
        if root.val < L:
            return root.right 
        if root.val > R:
            return root.left
        return root