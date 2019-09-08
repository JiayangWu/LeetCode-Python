# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root_val = postorder[-1]
        root_idx = inorder.index(root_val)
        
        postorder_left = postorder[:root_idx]
        postorder_right = postorder[root_idx:-1]
        
        inorder_left = inorder[:root_idx]
        inorder_right = inorder[root_idx + 1:]
        
        # print preorder_left, preorder_right, inorder_left, inorder_right
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        
        return root