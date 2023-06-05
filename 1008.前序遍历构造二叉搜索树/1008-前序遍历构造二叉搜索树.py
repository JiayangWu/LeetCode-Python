# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        hasRight = False
        for i, val in enumerate(preorder):
            if val > root.val:
                right_index = i
                hasRight = True
                break
        
        
        if hasRight:
            root.left = self.bstFromPreorder(preorder[1:right_index])
            root.right = self.bstFromPreorder(preorder[right_index:])
        else:
            root.left = self.bstFromPreorder(preorder[1:])
        return root

