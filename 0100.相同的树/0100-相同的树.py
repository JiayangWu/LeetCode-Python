# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        self.result = True
        self.check(p,q)
        return self.result
    
    def check(self, p, q):
        # if :
        if (not p or not q)  or (p.val != q.val)  :
            self.result = False
            return 

        if p.left or q.left:
            self.check(p.left, q.left)
        if p.right or q.right:
            self.check(p.right, q.right)
        
        return