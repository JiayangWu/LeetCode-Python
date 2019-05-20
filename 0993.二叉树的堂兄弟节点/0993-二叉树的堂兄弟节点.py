# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val == x or root.val == y:
            return False
        x_father = self.findFather(root, x)
        y_father = self.findFather(root, y)
        x_depth = self.findDepth(root, x)
        y_depth = self.findDepth(root, y)
        # print x_father.val, y_father.val,x_depth,y_depth
        
        return x_depth == y_depth and x_father != y_father
    
    def findDepth(self, node, value):
        if not node:
            return -100
        # print node.val,value
        if node.val  == value:
            return 0
        else:
            return 1 + max(self.findDepth(node.left, value), self.findDepth(node.right, value))
        
    def findFather(self, node, value):
        if not node:
            return 
       
        if node.left:
            if node.left.val == value:
                return node
        if node.right:
            if node.right.val == value:
                return node
        return self.findFather(node.right, value) or self.findFather(node.left, value)
        
        
        