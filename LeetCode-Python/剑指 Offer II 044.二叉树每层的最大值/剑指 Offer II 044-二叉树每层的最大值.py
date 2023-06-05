# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        queue = [root]
        res = []

        while queue:
            next_queue = []
            max_val = float("-inf")
            for node in queue:
                if node:
                    max_val = max(max_val, node.val)
                    next_queue.extend([node.left, node.right])

            queue = next_queue
            if max_val != float("-inf"):
                res.append(max_val)

        return res