# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #ÓÒÖÐ×óµÄ±éÀúË³Ðò
        if not root:
            return root
        self.s = 0
        
        def convert(node):
            if not node:
                return 
            
            convert(node.right)
            node.val += self.s
            self.s = node.val
            convert(node.left)
            
        convert(root)
        return root