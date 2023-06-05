# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         queue = [root]
#         while queue:
#             next_queue = []
#             level_val = []
#             for node in queue:
#                 if node:
#                     next_queue.append(node.left)
#                     next_queue.append(node.right)
#                     level_val.append(node.val)
#                 else:
#                     level_val.append("n")
            
#             if level_val != level_val[::-1]:
#                 return False
#             queue = next_queue[:]
#         return True

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left:Optional[TreeNode], right: Optional[TreeNode]):
            if not left:
                return not right
            if not right:
                return not left
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root.left, root.right)
