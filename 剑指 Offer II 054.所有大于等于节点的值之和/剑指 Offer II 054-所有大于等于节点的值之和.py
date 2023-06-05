# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def convertBST(self, root: TreeNode) -> TreeNode:

#         def inOrderGetSum(node):
#             if not node:
#                 return 0
#             return node.val + inOrderGetSum(node.left) + inOrderGetSum(node.right)

#         self.cur_sum = 0
#         def inOrderSetVal(node, total_sum):
#             if not node:
#                 return 0

#             original_node_val = node.val
#             inOrderSetVal(node.left, total_sum)
#             node.val = total_sum - self.cur_sum
#             self.cur_sum += original_node_val
#             right_subtree_sum = inOrderSetVal(node.right, total_sum)


#         total_sum = inOrderGetSum(root)
#         inOrderSetVal(root, total_sum)
#         return root


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # right - root - left
        self.cur_sum = 0
        def reverseInorder(node):
            if not node:
                return 

            reverseInorder(node.right)
            self.cur_sum += node.val
            node.val = self.cur_sum
            reverseInorder(node.left)

        reverseInorder(root)
        return root
