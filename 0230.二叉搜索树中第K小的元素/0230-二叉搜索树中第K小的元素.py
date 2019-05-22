# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        inorder = list()
        self.inorderTra(root, inorder)
        print inorder
        
        return inorder[k-1]
    
    def inorderTra(self, node, path):
        if not node:
            return 
        self.inorderTra(node.left, path)
        path.append(node.val)
        self.inorderTra(node.right, path)