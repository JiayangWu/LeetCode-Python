# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)
        
        inorder = inOrder(root)
        return len(inorder) == len(set(inorder)) and inorder == sorted(inorder)