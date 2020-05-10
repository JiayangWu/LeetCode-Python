# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if not s and not t:
            return True
        if s and not t:
            return False
        if t and not s:
            return False

        return self.isSameTree(t, s) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        if t1 and not t2:
            return False
        if t2 and not t1:
            return False
        return t1.val == t2.val and self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)