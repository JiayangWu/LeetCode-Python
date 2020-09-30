# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def isSame(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            if node1 and not node2:
                return False
            return node1.val == node2.val and isSame(node1.left, node2.right) and isSame(node1.right, node2.left)

        return isSame(root, root)