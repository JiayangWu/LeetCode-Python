# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        res = []

        while queue:
            next_queue = []
            cur_level = []
            for node in queue:
                if node:
                    cur_level.append(node.val)

                    if node.left:
                        next_queue.append(node.left)
                    if node.right:
                        next_queue.append(node.right)

            if cur_level:
                res.append(cur_level[-1])
            queue = next_queue

        return res