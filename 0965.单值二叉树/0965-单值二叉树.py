# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
            
        self.value = root.val
        self.result = True
        self.generate(root)
        return self.result
    
    def generate(self, root):
        if root.val != self.value:
            self.result = False
            return
        if not root:
            return 
        if root.left:
            self.generate(root.left)
        if root.right:
            self.generate(root.right)