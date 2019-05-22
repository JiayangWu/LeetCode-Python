# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list() 
        self.generate(root, result)
        return result


    
    def generate(self, root, result):
        
        if not root:
            return 
        
        if root.left:
            self.generate(root.left, result)
            
        result.append(root.val)

        if root.right:
            self.generate(root.right, result)
