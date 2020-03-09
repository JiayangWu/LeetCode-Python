# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        return inorder(root)[-k]
#         self.res = None
#         def dfs(node, left):
#             if not node:
#                 return None

#             if not self.res:
#                 dfs(node.right, left)
#                 if node.right:
#                     left -= 1
#                 if left == 1:
#                     self.res = node.val
#                     return
#                 dfs(node.left, left - 1)
            
#         dfs(root, k)
#         return self.res