# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root_val = postorder[-1]
        root_index_inorder = inorder.index(root_val)

        left_inorder = inorder[:root_index_inorder]
        right_inorder = inorder[root_index_inorder + 1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder): -1]

        root = TreeNode(root_val, self.buildTree(left_inorder, left_postorder), self.buildTree(right_inorder, right_postorder))
        return root