# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        survivor_nodes = set()

        def dfs(node, path):
            if not node:
                return
            # path.append(node)
            if not node.left and not node.right:
                path.append(node)
                path_sum = 0
                for n in path:
                    path_sum += n.val
                if path_sum >= limit:
                    for n in path:
                        survivor_nodes.add(n)
                return
            dfs(node.left, path + [node])
            dfs(node.right, path + [node])

        dfs(root, [])
        # print(survivor_nodes)
        def killNodes(node):
            if not node:
                return
            
            if node.left not in survivor_nodes:
                node.left = None
            if node.right not in survivor_nodes:
                node.right = None

            killNodes(node.left)
            killNodes(node.right)

        if root not in survivor_nodes:
            return None
        killNodes(root)
        return root