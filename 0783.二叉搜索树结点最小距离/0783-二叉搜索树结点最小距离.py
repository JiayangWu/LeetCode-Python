# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            self.res = min(self.res, node.val - self.pre)
            self.pre = node.val
            inorder(node.right)
            
        self.pre = -99999
        self.res = 99999
        inorder(root)
        return self.res