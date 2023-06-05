# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.cur_sum = 0
        def backwardInorder(node):
            if not node:
                return 

            backwardInorder(node.right)
            self.cur_sum += node.val
            node.val = self.cur_sum
            backwardInorder(node.left)

        backwardInorder(root)
        return root