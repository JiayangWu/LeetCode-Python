# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        
        preorder_left = preorder[1:1 + root_idx]
        preorder_right = preorder[root_idx + 1:]
        
        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx + 1:]
        
        # print preorder_left, preorder_right, inorder_left, inorder_right
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root