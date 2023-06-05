# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        
        if not root:
            return 0
        if L <= root.val <= R:
            res += root.val
        if root.val < R:
            res += self.rangeSumBST(root.right, L, R)
        if root.val > L:
            res += self.rangeSumBST(root.left, L, R)
            
        return res
                