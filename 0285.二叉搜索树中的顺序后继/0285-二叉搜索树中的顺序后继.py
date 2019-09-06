# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node] + inorder(node.right)
        l = inorder(root)
        i = l.index(p)
        return l[i + 1] if i < len(l) - 1 else None