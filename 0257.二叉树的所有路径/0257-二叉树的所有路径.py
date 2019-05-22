# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return list()
        
        res = list()
        temp_res = str(root.val)
        
        if not root.left and not root.right:
            return [temp_res]
        
        self.generate(root.left, str(root.val), res)
        self.generate(root.right, str(root.val), res)
        
        return res
    
    def generate(self, node, temp_res, res):
        if not node:
            return
        temp_res += "->" + str(node.val)
        
        if not node.left and not node.right:
            res.append(temp_res)
            return
        else:           
            self.generate(node.left, temp_res, res)
            self.generate(node.right, temp_res, res)
            
        return 
        