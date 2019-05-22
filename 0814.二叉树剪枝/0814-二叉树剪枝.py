# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # print root.val,  self.generate(root.left), self.generate(root.right)
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left == None and root.right == None and (root.val == 0):
            return None
        return root
    
            
