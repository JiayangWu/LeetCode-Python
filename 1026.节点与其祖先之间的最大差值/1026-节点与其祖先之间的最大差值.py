# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s = 0
        
        def find(node, path):
            if not node:                
                return 

            tmp = max(abs(max(path) - node.val), abs(min(path) - node.val))
            self.s = max(self.s, tmp)
            
            path.append(node.val)
            
            find(node.left, path)
            find(node.right, path)
            
            path.pop()
            
        find(root, [root.val])
        return self.s