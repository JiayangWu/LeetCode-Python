# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.append(node.right)
                stack.append(node.val)
                stack.append(node.left)
            elif isinstance(node, int):
                res.append(node)
        return res