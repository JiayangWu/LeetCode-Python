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
        inorder = sorted(preorder)
        
        return self.buildTree(preorder, inorder)
        
        
        
    def buildTree(self, preorder, inorder): # leetcode 105
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])        
        left_inorder = inorder[: inorder.index(root.val)]
        right_inorder = inorder[inorder.index(root.val) + 1 :]
        
        l_left = len(left_inorder)
        left_preorder = preorder[1:l_left + 1]
        right_preorder = preorder[l_left + 1 :]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root