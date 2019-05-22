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
        inorder = list() 
        self.inorderTra(root, inorder)
        # print inorder
        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True
    
    def inorderTra(self, root, inorder):
        if not root:
            return None
    
        
        self.inorderTra(root.left, inorder)
        inorder.append(root.val)
        self.inorderTra(root.right, inorder)
        
        return 
        