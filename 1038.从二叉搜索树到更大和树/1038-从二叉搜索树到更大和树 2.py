# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.right)
            self.sum += node.val
            node.val = self.sum
            inorder(node.left)
            
        inorder(root)
        return root