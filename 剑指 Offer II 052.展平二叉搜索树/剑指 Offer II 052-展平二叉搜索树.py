# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        inorder_list = inorder(root)

        dummy = TreeNode(-1)
        p = dummy
        for val in inorder_list:
            p.right = TreeNode(val)
            p = p.right
        
        return dummy.right
