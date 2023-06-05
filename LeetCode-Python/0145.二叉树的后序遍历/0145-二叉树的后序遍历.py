# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.val, node.right, node.left])
            elif isinstance(node, int):
                res.append(node)

        return res