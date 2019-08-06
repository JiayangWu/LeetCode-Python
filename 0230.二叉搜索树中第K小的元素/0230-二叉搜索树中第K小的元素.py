# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        def inorderTraversal(node):
            if not node:
                return []
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
        
        l = inorderTraversal(root)
        return l[k - 1]