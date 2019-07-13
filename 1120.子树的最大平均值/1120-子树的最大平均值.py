# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        if not root:
            return 0
        
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        Inorder = inorder(root)
        return max(1.0 * sum(Inorder) / len(Inorder), self.maximumAverageSubtree(root.left), self.maximumAverageSubtree(root.right))
