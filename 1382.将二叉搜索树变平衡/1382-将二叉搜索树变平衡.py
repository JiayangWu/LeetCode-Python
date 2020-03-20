# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        l = inorder(root)
        
        def generator(l):
            if not l:
                return None
            idx = len(l) // 2
            root = TreeNode(l[idx])
            root.left = generator(l[:idx])
            root.right = generator(l[idx + 1:])
            return root
            
        return generator(l)