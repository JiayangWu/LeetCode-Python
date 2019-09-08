# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)
        
        inorder = inOrder(root)
        inorder.sort()
        
        self.idx = 0
        def change(node):
            if not node:
                return
            change(node.left)
            node.val = inorder[self.idx]
            self.idx += 1
            change(node.right)
            
        change(root)
        return root
            