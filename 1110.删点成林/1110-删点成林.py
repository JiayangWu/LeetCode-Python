# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = [] 
        def dfs(node, node_is_new_root):
            if not node:
                return
            left = node.left
            right = node.right
            if node_is_new_root and node.val not in to_delete:
                res.append(node)
            if left and left.val in to_delete:
                node.left = None
            if right and right.val in to_delete:
                node.right = None
             
            dfs(left, node.val in to_delete)
            dfs(right, node.val in to_delete)
        dfs(root, True)
        return res
                