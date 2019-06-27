# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #每一个节点变成其左孩子的右节点        
        if not root or (not root.left and not root.right):
            return root

        parent, sibling = None, None
        while root:
            tmp = root.left
            root.left = sibling
            
            sibling = root.right
            root.right = parent
            
            parent = root
            root = tmp
            
        return parent
            
            
