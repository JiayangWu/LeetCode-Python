# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.res = None
        def inorder(node):
            if not node or self.res:
                return 

            inorder(node.left)
            if node.val == val:
                self.res = node
            inorder(node.right)

        inorder(root)
        return self.res