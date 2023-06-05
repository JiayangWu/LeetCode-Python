# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        visited = set()
        self.res = False

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            
            if k - node.val in visited:
                self.res = True
            visited.add(node.val)
            
            if not self.res:
                inorder(node.right)
        
        inorder(root)
        return self.res
            
