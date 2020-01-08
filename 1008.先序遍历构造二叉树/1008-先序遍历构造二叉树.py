# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None 
        inorder = sorted(preorder)

        idx = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.bstFromPreorder(preorder[1:idx + 1])
        root.right = self.bstFromPreorder(preorder[idx + 1:])
        return root